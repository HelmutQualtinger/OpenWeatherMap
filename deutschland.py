orte = [
    ("Berlin", "Berlin", "DE"),
    ("Hamburg", "Hamburg", "DE"),
    ("München", "Bayern", "DE"),
    ("Köln", "Nordrhein-Westfalen", "DE"),
    ("Frankfurt am Main", "Hessen", "DE"),
    ("Stuttgart", "Baden-Württemberg", "DE"),
    ("Düsseldorf", "Nordrhein-Westfalen", "DE"),
    ("Dortmund", "Nordrhein-Westfalen", "DE"),
    ("Essen", "Nordrhein-Westfalen", "DE"),
    ("Leipzig", "Sachsen", "DE"),
    ("Bremen", "Bremen", "DE"),
    ("Dresden", "Sachsen", "DE"),
    ("Hannover", "Niedersachsen", "DE"),
    ("Nürnberg", "Bayern", "DE"),
    ("Duisburg", "Nordrhein-Westfalen", "DE"),
    ("Bochum", "Nordrhein-Westfalen", "DE"),
    ("Wuppertal", "Nordrhein-Westfalen", "DE"),
    ("Bielefeld", "Nordrhein-Westfalen", "DE"),
    ("Bonn", "Nordrhein-Westfalen", "DE"),
    ("Münster", "Nordrhein-Westfalen", "DE"),
    ("Karlsruhe", "Baden-Württemberg", "DE"),
    ("Mannheim", "Baden-Württemberg", "DE"),
    ("Augsburg", "Bayern", "DE"),
    ("Wiesbaden", "Hessen", "DE"),
    ("Gelsenkirchen", "Nordrhein-Westfalen", "DE"),
    ("Mönchengladbach", "Nordrhein-Westfalen", "DE"),
    ("Braunschweig", "Niedersachsen", "DE"),
    ("Kiel", "Schleswig-Holstein", "DE"),
    ("Chemnitz", "Sachsen", "DE"),
    ("Aachen", "Nordrhein-Westfalen", "DE"),
    ("Halle (Saale)", "Sachsen-Anhalt", "DE"),
    ("Magdeburg", "Sachsen-Anhalt", "DE"),
    ("Freiburg im Breisgau", "Baden-Württemberg", "DE"),
    ("Krefeld", "Nordrhein-Westfalen", "DE"),
    ("Lübeck", "Schleswig-Holstein", "DE"),
    ("Oberhausen", "Nordrhein-Westfalen", "DE"),
    ("Erfurt", "Thüringen", "DE"),
    ("Mainz", "Rheinland-Pfalz", "DE"),
    ("Rostock", "Mecklenburg-Vorpommern", "DE"),
    ("Kassel", "Hessen", "DE"),
    ("Hagen", "Nordrhein-Westfalen", "DE"),
    ("Saarbrücken", "Saarland", "DE"),
    ("Hamm", "Nordrhein-Westfalen", "DE"),
    ("Mülheim an der Ruhr", "Nordrhein-Westfalen", "DE"),
    ("Ludwigshafen am Rhein", "Rheinland-Pfalz", "DE"),
    ("Potsdam", "Brandenburg", "DE"),
    ("Leverkusen", "Nordrhein-Westfalen", "DE"),
    ("Oldenburg", "Niedersachsen", "DE"),
    ("Osnabrück", "Niedersachsen", "DE"),
    ("Solingen", "Nordrhein-Westfalen", "DE"),
    ("Heidelberg", "Baden-Württemberg", "DE"),
    ("Herne", "Nordrhein-Westfalen", "DE"),
    ("Neuss", "Nordrhein-Westfalen", "DE"),
    ("Darmstadt", "Hessen", "DE"),
    ("Paderborn", "Nordrhein-Westfalen", "DE"),
    ("Regensburg", "Bayern", "DE"),
    ("Ingolstadt", "Bayern", "DE"),
    ("Würzburg", "Bayern", "DE"),
    ("Fürth", "Bayern", "DE"),
    ("Wolfsburg", "Niedersachsen", "DE"),
    ("Offenbach am Main", "Hessen", "DE"),
    ("Ulm", "Baden-Württemberg", "DE"),
    ("Heilbronn", "Baden-Württemberg", "DE"),
    ("Pforzheim", "Baden-Württemberg", "DE"),
    ("Göttingen", "Niedersachsen", "DE"),
    ("Bottrop", "Nordrhein-Westfalen", "DE"),
    ("Recklinghausen", "Nordrhein-Westfalen", "DE"),
    ("Reutlingen", "Baden-Württemberg", "DE"),
    ("Bremerhaven", "Bremen", "DE"),
    ("Koblenz", "Rheinland-Pfalz", "DE"),
    ("Bergisch Gladbach", "Nordrhein-Westfalen", "DE"),
    ("Jena", "Thüringen", "DE"),
    ("Remscheid", "Nordrhein-Westfalen", "DE"),
    ("Erlangen", "Bayern", "DE"),
    ("Moers", "Nordrhein-Westfalen", "DE"),
    ("Siegen", "Nordrhein-Westfalen", "DE"),
    ("Hildesheim", "Niedersachsen", "DE"),
    ("Salzgitter", "Niedersachsen", "DE"),
    ("Kaiserslautern", "Rheinland-Pfalz", "DE"),
    ("Witten", "Nordrhein-Westfalen", "DE"),
    ("Gütersloh", "Nordrhein-Westfalen", "DE"),
    ("Iserlohn", "Nordrhein-Westfalen", "DE")
]

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