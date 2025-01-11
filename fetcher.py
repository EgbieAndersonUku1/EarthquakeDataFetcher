import requests
from tenacity import retry, stop_after_attempt, wait_exponential
import pandas as pd

from custom_error import FetchDataNotFoundError, EarthQuakeDataNotFound



class EarthquakeFetcher:
    NUM_OF_ATTEMPTS  = 3
    MIN_SECS_TO_WAIT = 4
    MAX_SECS_TO_WAIT = 10

    def __init__(self, url):
        self.url   = url
        self.cache = None

    @classmethod
    def set_retry_attempts(cls, num_of_attempts: int = 3, min_secs_to_wait: int = 4, max_secs_to_wait: int = 10):
        """
        Sets the number of retry attempts and the wait time before each re-attempt.

        This method must be called before the `EarthquakeFetcher`as a class method before is initialized in order 
        to configure the retry parameters. If this method is not called, the default retry settings 
        will be used.

        Args:
            num_of_attempts (int): The number of retry attempts. Default is 3.
            min_secs_to_wait (int): The minimum number of seconds to wait before retrying. Default is 4.
            max_secs_to_wait (int): The maximum number of seconds to wait before retrying. Default is 10.

        Returns:
            None: This method does not return any value but updates the class-level retry settings.

        Example usage:

        # when set
        >>> EarthquakeFetcher.set_retry_attempts(num_of_attempts=5, min_secs_to_wait=2, max_secs_to_wait=8)
        >>> fetcher = EarthquakeFetcher("https://example.com")
        >>> fetcher.fetch_data()
        >>> data = fetcher.get_earthquake_data()

        # default usage without setting
        >>> fetcher = EarthquakeFetcher("https://example.com")
        >>> fetcher.fetch_data()
        >>> data = fetcher.get_earthquake_data()
        """
        
        cls.NUM_OF_ATTEMPTS = num_of_attempts
        cls.MIN_SECS_TO_WAIT = min_secs_to_wait
        cls.MAX_SECS_TO_WAIT = max_secs_to_wait
        
    @retry(stop=stop_after_attempt(NUM_OF_ATTEMPTS), 
           wait=wait_exponential(multiplier=1, min=MIN_SECS_TO_WAIT, max=MAX_SECS_TO_WAIT))
    def fetch_data(self) -> None:
        """
        Fetches data from the specified URL and stores it in the local cache.

        This method uses an exponential backoff retry mechanism. If fetching the data fails 
        on the first attempt, it retries up to `NUM_OF_ATTEMPTS` times, waiting between 
        `MIN_SECS_TO_WAIT` and `MAX_SECS_TO_WAIT` seconds between attempts.

        If all attempts fail, the method raises a `requests.exceptions.RequestException`.

        Returns:
            None: This method does not return data but stores it in the local cache.
        """
        if self.cache is None:
            try:
                response = requests.get(self.url)
                response.raise_for_status()  
                self.cache = response.json()  
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                raise  # Re-raise the exception to trigger retry
        else:
            print("getting from cache...")
    
    def get_earthquake_data(self, num_of_rows_to_retrieve:int = 10) -> pd.DataFrame:
        """
        Retrieves earthquake data as a pandas DataFrame.

        This method processes cached earthquake data into rows and columns. The number of rows 
        returned is determined by the `num_of_rows_to_retrieve` parameter, with a default of 10. 
        Note in order for the method to fetch the data the `fetch_data` method must be called first to populate the cache; 
        otherwise, this method will raise an error.

        Args:
            num_of_rows_to_retrieve (int): Number of rows to return. Default is 10.

        Returns:
            pd.DataFrame: A DataFrame containing the requested number of rows.

        Raises:
            FetchDataNotFoundError: If the cache is empty, typically because `fetch_data` was 
            not called before this method.

            EarthQuakeDataNotFound: If no earthquake data is found in the `features` key of 
            the cache.
        """
        if not self.cache:
            raise FetchDataNotFoundError(
                "Error: Data not found. Try running `fetch_data` before calling this method."
            )
        
        earthquake_features = self.cache.get("features", [])
      
        if not earthquake_features:
            raise EarthQuakeDataNotFound("No earthquake data found in the `features` key.")
        
        # df = dataframe
        df = pd.json_normalize(earthquake_features)
        return df.head(num_of_rows_to_retrieve)
        