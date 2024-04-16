
austrian_cities_german = [
    ("Wien", "Wien", "AT"),
    ("Graz", "Steiermark", "AT"),
    ("Linz", "Oberösterreich", "AT"),
    ("Salzburg", "Salzburg", "AT"),
    ("Innsbruck", "Tirol", "AT"),
    # Add more cities here...
    ("Klagenfurt", "Kärnten", "AT"),
    ("St. Pölten", "Niederösterreich", "AT"),
    ("Eisenstadt", "Burgenland", "AT"),
    ("Bregenz", "Vorarlberg", "AT"),
    ("Villach", "Kärnten", "AT"),
    # Add more cities here...
    ("Gmunden", "Oberösterreich", "AT"),
    ("Kufstein", "Tirol", "AT"),
    ("Baden", "Niederösterreich", "AT"),
    ("Dornbirn", "Vorarlberg", "AT"),
    ("Krems", "Niederösterreich", "AT"),
    ("Steyr", "Oberösterreich", "AT"),
    ("Wiener Neustadt", "Niederösterreich", "AT"),
    ("Vöcklabruck", "Oberösterreich", "AT"),
    ("Wolfsberg", "Kärnten", "AT"),
    ("Leoben", "Steiermark", "AT"),
    ("Kapfenberg", "Steiermark", "AT"),
    ("Amstetten", "Niederösterreich", "AT"),
    ("Feldkirch", "Vorarlberg", "AT"),
    ("Hallein", "Salzburg", "AT"),
    ("Wels", "Oberösterreich", "AT"),
    ("Sankt Veit an der Glan", "Kärnten", "AT"),
    ("Traun", "Oberösterreich", "AT"),
    ("Klosterneuburg", "Niederösterreich", "AT"),
    ("Schwechat", "Niederösterreich", "AT"),
    ("Tulln", "Niederösterreich", "AT"),
    ("Spittal an der Drau", "Kärnten", "AT"),
    ("Saalfelden", "Salzburg", "AT"),
    ("Ansfelden", "Oberösterreich", "AT"),
    ("Stockerau", "Niederösterreich", "AT"),
    ("Telfs", "Tirol", "AT"),
    ("Bad Ischl", "Oberösterreich", "AT"),
    ("Bludenz", "Vorarlberg", "AT"),
    ("Götzis", "Vorarlberg", "AT"),
    ("Ebreichsdorf", "Niederösterreich", "AT"),
    ("Marchtrenk", "Oberösterreich", "AT"),
    ("Korneuburg", "Niederösterreich", "AT"),
    ("Neunkirchen", "Niederösterreich", "AT"),
    ("Hard", "Vorarlberg", "AT"),
    ("Zwettl", "Niederösterreich", "AT"),
    ("Lienz", "Tirol", "AT"),
    ("Rankweil", "Vorarlberg", "AT"),
    ("Hohenems", "Vorarlberg", "AT"),
    ("Bruck an der Mur", "Steiermark", "AT"),
    ("Ternitz", "Niederösterreich", "AT"),
    ("Perchtoldsdorf", "Niederösterreich", "AT"),
    ("Krems an der Donau", "Niederösterreich", "AT"),
    ("Kapfenberg", "Steiermark", "AT"),
    ("Schwaz", "Tirol", "AT"),
    ("Hall in Tirol", "Tirol", "AT"),
    ("Gmünd", "Niederösterreich", "AT"),
    ("Wörgl", "Tirol", "AT"),
    ("Lustenau", "Vorarlberg", "AT"),
    ("Mödling", "Niederösterreich", "AT"),
    ("Hollabrunn", "Niederösterreich", "AT"),
    ("Schärding", "Oberösterreich", "AT"),
    ("Enns", "Oberösterreich", "AT"),
    ("Kufstein", "Tirol", "AT"),
    ("Bischofshofen", "Salzburg", "AT"),
    ("Gänserndorf", "Niederösterreich", "AT"),
    ("Villach", "Kärnten", "AT"),
    ("Ried im Innkreis", "Oberösterreich", "AT"),
    ("Knittelfeld", "Steiermark", "AT"),
    ("Trofaiach", "Steiermark", "AT"),
    ("Waidhofen an der Ybbs", "Niederösterreich", "AT"),
    ("Mistelbach", "Niederösterreich", "AT"),
    ("Zell am See", "Salzburg", "AT"),
    ("Seekirchen am Wallersee", "Salzburg", "AT"),
    ("Eisenstadt", "Burgenland", "AT"),
    ("Bregenz", "Vorarlberg", "AT"),
    ("Dornbirn", "Vorarlberg", "AT"),
    ("Krems", "Niederösterreich", "AT"),
    ("Gmunden", "Oberösterreich", "AT"),
    ("Klagenfurt", "Kärnten", "AT"),
    ("St. Pölten", "Niederösterreich", "AT"),
    ("Eisenstadt", "Burgenland", "AT"),
    ("Bregenz", "Vorarlberg", "AT"),
    ("Villach", "Kärnten", "AT"),
    ("Gmunden", "Oberösterreich", "AT"),
    ("Kufstein", "Tirol", "AT"),
    ("Baden", "Niederösterreich", "AT"),
    ("Dornbirn", "Vorarlberg", "AT"),
    ("Krems", "Niederösterreich", "AT"),
    ("Mattersburg", "Burgenland", "AT"),
    ("Retz", "Niederösterreich", "AT"),
    ("Oberwart", "Burgenland", "AT"),
    ("Mattersburg", "Burgenland", "AT")
]
print (len(austrian_cities_german))

unique_cities = list(set(austrian_cities_german))

print(len(unique_cities))

sorted_cities = sorted(unique_cities, key=lambda x: (x[1], x[0]))
for c in sorted_cities:
    print(c)
    
import mysql.connector
from credentials import *

def insert_into_location_table(sorted_cities):

    # Connect to the database
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    # Create the location_table if it doesn't exist

    # Insert the sorted city list into the location_table
    for city in sorted_cities:
        cursor.execute("INSERT INTO location_table (city, canton, country) VALUES (%s, %s, %s)", city)
        conn.commit()

    # Commit the changes and close the connection
 
    conn.close()
    
insert_into_location_table(sorted_cities)