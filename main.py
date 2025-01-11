
from fetcher import EarthquakeFetcher

# Example usage:

def main():
    URL     = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
    fetcher = EarthquakeFetcher(URL)

    fetcher.fetch_data()
    data = fetcher.get_earthquake_data()

    print(data)
    
    # check to see if it using cache when called again
    # fetcher.fetch_data()
    # fetcher.fetch_data()
    

if __name__  == "__main__":
    main()