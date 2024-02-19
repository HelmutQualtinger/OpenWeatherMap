
"""
Dieses Modul ruft Wetterdaten von der OpenWeatherMap-API ab und speichert sie in einer MySQL-Datenbank.
"""

import time
import json
import requests
import mysql.connector
import schedule

# 


# Read the credentials from the secret JSON file
with open('secret.json') as file:
    credentials = json.load(file)

# Extract the API key and database credentials from the JSON object
API_KEY = credentials['api_key']
DB_HOST = credentials['db_host']
DB_USER = credentials['db_user']
DB_PASSWORD = credentials['db_password']
DB_NAME = credentials['db_name']
def fetch_and_save_weather_data():
    """
    Ruft Wetterdaten von der OpenWeatherMap-API ab und speichert sie in einer MySQL-Datenbank.

    Parameters:
        None

    Returns:
        None
    """
    # Specify the city for which you want to fetch weather data
    city = "London"

    # Query the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract the required measurements from the API response
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    # Connect to the MySQL database
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
            city VARCHAR(255),
            temperature FLOAT,
            humidity INT,
            pressure INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_timestamp (timestamp)
        )
    """
    cursor.execute(create_table_query)

    # Insert the weather data into the database
    insert_data_query = """
        INSERT INTO weather_data (city, temperature, humidity, pressure)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_data_query, (city, temperature, humidity, pressure))
    db.commit()

    # Close the database connection
    cursor.close()
    db.close()

# Schedule the execution of the fetch_and_save_weather_data function every hour
schedule.every().hour.do(fetch_and_save_weather_data)

# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)