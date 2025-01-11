### Overview

Retrieves real-time earthquake data from the USGS (United States Geological Survey) API, showcasing the 10 most powerful earthquakes from the past week. It provides valuable insights into global seismic activity, highlighting significant events worldwide.

### How the Program Works

The program sends an API request to the USGS endpoint:

https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson


This API returns a dataset of global earthquakes that occurred in the past week.

The program processes the response and displays information about the 10 strongest earthquakes of the week, including key details such as:

- Location
- Magnitude
- link for more information about each earthquake
- and more

### How to Run the Project

1. **Clone the Repository**  
   First, clone the project to your local machine:


This API returns a dataset of global earthquakes that occurred in the past week.

The program processes the response and displays information about the 10 strongest earthquakes of the week, including key details such as:

- Location
- Magnitude
- A direct link for more information about each earthquake

### How to Run the Project

1. **Clone the Repository**  
   First, clone the project to your local machine:

   git clone https://github.com/EgbieAndersonUku1/EarthquakeDataFetcher.git .
 


2. **(Optional) Create a Virtual Environment**  
Create a virtual environment for the project:


3. **Activate the Virtual Environment**  
- **For Windows**:  
  ```
  .\venv\Scripts\activate.ps1
  ```

- **For macOS/Linux**:  
  ```
  source venv/bin/activate
  ```

4. **Install Dependencies**  
Install the necessary packages from the `requirements.txt` file by running:

```
 pip install -r requirements.txt
```
 


5. **Run the Program**  
Finally, run the program:


Further future enhancement:
- Show the Earthquake on a worldwide map with points representing the Earthquake for better visually representation

