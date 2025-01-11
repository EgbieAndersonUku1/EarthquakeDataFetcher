import asyncio

from fetcher import EarthquakeFetcher

# Example usage:

async def main():
    URL     = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
    fetcher = EarthquakeFetcher(URL)

    await fetcher.fetch_data()
    data = fetcher.get_earthquake_data()

    print(data)
    
   

if __name__  == "__main__":
    asyncio.run(main())