import mysql.connector
from credentials import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# Connect to the MySQL database
def fetch_location_data():
    
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch the data
    query = "SELECT distinct city, canton, country FROM location_table"
    cursor.execute(query)

    # Fetch all the rows from the result set
    results = cursor.fetchall()
    cursor.close()
    db.close()

    # Print the data
    for row in results:
        city, canton, country = row
        print(f"City: {city}, Canton: {canton}, Country: {country}")
        yield( city, canton, country)

    # Close the cursor and database connection

# Call the function to fetch and print location data
if __name__ == "__main__":
    for i,(city,canton,country) in enumerate(fetch_location_data()):
        print (f"Got {i} {city}, {canton}, {country} from location_table")