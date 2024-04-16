
"""
Dieses Modul ruft Wetterdaten von der OpenWeatherMap-API ab und speichert sie in einer MySQL-Datenbank.
"""
import time
import requests
import json
import mysql.connector
import schedule
import datetime
from credentials import API_KEY, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from readLocationDB import fetch_location_data
# import schweiz
# import deutschland
# import italia
# import france


# Extract the API key and database credentials from the JSON object
def fetch_and_save_weather_data():
    """
    Ruft Wetterdaten von der OpenWeatherMap-API ab und speichert sie in einer MySQL-Datenbank.

    Parameters:
        None

    Returns:
        None
    """
    db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    cursor = db.cursor()

        # Create the weather_data table if it does not exist
    create_table_query = """
            CREATE TABLE IF NOT EXISTS weather_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city VARCHAR(40),
                lon FLOAT,
                lat FLOAT,
                weather_main VARCHAR(25),
                weather_desc VARCHAR(25),
                temperature FLOAT,
                temperature_min FLOAT,
                temperature_max FLOAT,
                temperature_feels_like FLOAT,
                humidity FLOAT,
                pressure FLOAT,
                wind_speed FLOAT,
                wind_direction FLOAT,
                rain_down_1h FLOAT,
                clouds FLOAT,
                country VARCHAR(25),
                canton VARCHAR(25),
                dt TIMESTAMP,
                sunrise TIMESTAMP,
                sunset TIMESTAMP,
                tz float,
                time_inserted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                INDEX idx_timestamp (time_inserted),
                index idx_city (city),
                index idx_canton (canton),
                index idx_country (country),
                index idx_dt (dt)
            )
        """
    returnv = cursor.execute(create_table_query)

    # Query the OpenWeatherMap API
    # 
    for (city, canton, country) in fetch_location_data():
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&lang=de&appid={API_KEY}"
        print (url)
        response = requests.get(url)
        data = response.json()
   #     print (response)
        # Dump the API response to a JSON file
        with open('response.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
        # Extract the required measurements from the API response
        try:
            lon= data["coord"]["lon"]
            lat= data["coord"]["lat"]
            weather_main = data["weather"][0]["description"]
            weather_desc = data["weather"][0]["main"]
            temperature = data["main"]["temp"] -273.15
            temperature_min = data["main"]["temp_min"] -273.15
            temperature_max = data["main"]["temp_max"] -273.15
            temperature_feels_like = data["main"]["feels_like"] -273.15
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"]
            wind_direction = data["wind"]["deg"]
            try:
                rain_down_1h = data["rain"]["1h"]
            except KeyError:
                rain_down_1h = 0
            dt= data["dt"]
            clouds = data["clouds"]["all"]
            country = data["sys"]["country"]
            sunrise = data["sys"]["sunrise"]
            sunset = data["sys"]["sunset"]
            country = data["sys"]["country"]
            city = data["name"][:25] # use city name called for instead
            tz = data["timezone"]
        # Convert unix timestamps to SQL timestamps
            sunrise = datetime.datetime.fromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S')
            sunset = datetime.datetime.fromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S')
            dt = datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
        # Connect to the MySQL database
        
        # Truncate weather_main to 25 characters
            weather_main = weather_main[:25]
        # Insert the weather data into the database
            insert_data_query = """
            INSERT INTO weather_data (
                city, 
                temperature, 
                temperature_min, 
                temperature_max, 
                temperature_feels_like, 
                humidity, 
                pressure, 
                lon, 
                lat, 
                weather_main, 
                weather_desc, 
                wind_speed, 
                wind_direction, 
                rain_down_1h, 
                clouds, 
                country,
                canton, 
                dt,
                sunrise,
                sunset,
                tz)
            VALUES (%s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s)  
        """
        # print (city, temperature, temperature_min, temperature_max, temperature_feels_like,
        #                 humidity, pressure, lon, lat, "--",weather_main,"--", 
        #                 weather_desc, wind_speed, wind_direction, rain_down_1h, clouds,
        #                 country, canton, dt, sunrise, sunset, tz)
            if len(canton)>25:
                    canton = canton[:25]
            cursor.execute(insert_data_query, 
                    (city, temperature, temperature_min, temperature_max, temperature_feels_like,
                        humidity, pressure, lon, lat, weather_main, 
                        weather_desc, wind_speed, wind_direction, rain_down_1h, clouds,
                        country, canton, dt, sunrise, sunset, tz))
            db.commit()
        except KeyError:
                pass
            
        time.sleep(0.05)

        # Close the database connection

    cursor.close()
    db.close()

fetch_and_save_weather_data()

# Schedule the fetch_and_save_weather_data function to run every hour
schedule.every().hour.at(":05").do(fetch_and_save_weather_data)
schedule.every().hour.at(":35").do(fetch_and_save_weather_data)

while True:
    schedule.run_pending()
    time.sleep(10)
