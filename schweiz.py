orte = [
    ('Flums', 'Königreich der Bösch', 'CH'),
    ('Simplon', 'Kaiserreich der Simpler', 'CH'),
    ('Vatikanstadt', 'Schweizer Garde', 'VA'),
    ("Zürich", "Zürich", 'CH'),
    ("Genf", "Genf", 'CH'),
    ("Basel", "Basel-Stadt", 'CH'),
    ("Bern", "Bern", 'CH'),
    ("Lausanne", "Waadt", 'CH'),
    ("Winterthur", "Zürich", 'CH'),
    ("Luzern", "Luzern", 'CH'),
    ("St. Gallen", "St. Gallen", 'CH'),
    ("Lugano", "Tessin", 'CH'),
    ("Biel/Bienne", "Bern", 'CH'),
    ("Thun", "Bern", 'CH'),
    ("Köniz", "Bern", 'CH'),
    ("La Chaux-de-Fonds", "Neuenburg", 'CH'),
    ("Schaffhausen", "Schaffhausen", 'CH'),
    ("Freiburg", "Freiburg", 'CH'),
    ("Chur", "Graubünden", 'CH'),
    ("Vernier", "Genf", 'CH'),
    ("Neuenburg", "Neuenburg", 'CH'),
    ("Uster", "Zürich", 'CH'),
    ("Sitten", "Wallis", 'CH'),
    ("Lancy", "Genf", 'CH'),
    ("Yverdon-les-Bains", "Waadt", 'CH'),
    ("Emmen", "Luzern", 'CH'),
    ("Zug", "Zug", 'CH'),
    ("Kriens", "Luzern", 'CH'),
    ("Rapperswil-Jona", "St. Gallen", 'CH'),
    ("Dübendorf", "Zürich", 'CH'),
    ("Dietikon", "Zürich", 'CH'),
    ("Montreux", "Waadt", 'CH'),
    ("Frauenfeld", "Thurgau", 'CH'),
    ("Wetzikon", "Zürich", 'CH'),
    ("Wil", "St. Gallen", 'CH'),
    ("Baar", "Zug", 'CH'),
    ("Meyrin", "Genf", 'CH'),
    ("Bulle", "Freiburg", 'CH'),
    ("Kreuzlingen", "Thurgau", 'CH'),
    ("Riehen", "Basel-Stadt", 'CH'),
    ("Renens", "Waadt", 'CH'),
    ("Nyon", "Waadt", 'CH'),
    ("Bellinzona", "Tessin", 'CH'),
    ("Vevey", "Waadt", 'CH'),
    ("Bülach", "Zürich", 'CH'),
    ("Aarau", "Aargau", 'CH'),
    ("Allschwil", "Basel-Landschaft", 'CH'),
    ("Spreitenbach", "Aargau", 'CH'),
    ("Volketswil", "Zürich", 'CH'),
    ("Carouge", "Genf", 'CH'),
    ("Wädenswil", "Zürich", 'CH'),
    ("Kloten", "Zürich", 'CH'),
    ("Pully", "Waadt", 'CH'),
    ("Thalwil", "Zürich", 'CH'),
    ("Wettingen", "Aargau", 'CH'),
    ("Regensdorf", "Zürich", 'CH'),
    ("Baden", "Aargau", 'CH'),
    ("Pratteln", "Basel-Landschaft", 'CH'),
    ("Morges", "Waadt", 'CH'),
    ("Adliswil", "Zürich", 'CH'),
    ("Wohlen", "Aargau", 'CH'),
    ("Muri bei Bern", "Bern", 'CH'),
    ("Oberwil", "Basel-Landschaft", 'CH'),
    ("Monthey", "Wallis", 'CH'),
    ("Zollikon", "Zürich", 'CH'),
    ("Brig-Glis", "Wallis", 'CH'),
    ("Horgen", "Zürich", 'CH'),
    ("Gossau", "St. Gallen", 'CH'),
    ("Steffisburg", "Bern", 'CH'),
    ("Horw", "Luzern", 'CH'),
    ("Locarno", "Tessin", 'CH'),
    ("Grenchen", "Solothurn", 'CH'),
    ("Uzwil", "St. Gallen", 'CH'),
    ("Binningen", "Basel-Landschaft", 'CH'),
    ("Ebikon", "Luzern", 'CH'),
    ("Schlieren", "Zürich", 'CH'),
    ("Aesch", "Basel-Landschaft", 'CH'),
    ("Muttenz", "Basel-Landschaft", 'CH'),
    ("Siders", "Wallis", 'CH'),
    ("Zofingen", "Aargau", 'CH'),
    ("Pfäffikon", "Zürich", 'CH'),
    ("Rüti", "Zürich", 'CH'),
    ("Arbon", "Thurgau", 'CH'),
    ("Weinfelden", "Thurgau", 'CH'),
    ("Altstätten", "St. Gallen", 'CH'),
    ("Brugg", "Aargau", 'CH'),
    ("Bassersdorf", "Zürich", 'CH'),
    ("Ittigen", "Bern", 'CH'),
    ("Zollikofen", "Bern", 'CH'),
    ("Olten", "Solothurn", 'CH'),
    ("Küsnacht", "Zürich", 'CH'),
    ("Gland", "Waadt", 'CH'),
    ("Cham", "Zug", 'CH'),
    ("Meilen", "Zürich", 'CH'),
    ("Amriswil", "Thurgau", 'CH'),
    ("Veyrier", "Genf", 'CH'),
    ("Worb", "Bern", 'CH'),
    ("Romanshorn", "Thurgau", 'CH'),
    ("Möhlin", "Aargau", 'CH'),
    ("Münchenstein", "Basel-Landschaft", 'CH')
]

# Alphabetically sorting the list based on city names
orte.sort(key=lambda x: (x[1],x[0]))

print(orte)


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
    
insert_into_location_table(orte)