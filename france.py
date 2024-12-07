import unicodedata

towns = [
    ("Paris", "Île-de-France", "FR"),
    ("Marseille", "Provence-Alpes-Côte d'Azur", "FR"),
    ("Lyon", "Auvergne-Rhône-Alpes", "FR"),
    ("Toulouse", "Occitanie", "FR"),
    ("Nice", "Provence-Alpes-Côte d'Azur", "FR"),
    ("Nantes", "Pays de la Loire", "FR"),
    ("Strasbourg", "Grand Est", "FR"),
    ("Montpellier", "Occitanie", "FR"),
    ("Bordeaux", "Nouvelle-Aquitaine", "FR"),
    ("Lille", "Hauts-de-France", "FR"),
    ("Rennes", "Brittany", "FR"),
    ("Reims", "Grand Est", "FR"),
    ("Le Havre", "Normandy", "FR"),
    ("Saint-Étienne", "Auvergne-Rhône-Alpes", "FR"),
    ("Toulon", "Provence-Alpes-Côte d'Azur", "FR"),
    ("Grenoble", "Auvergne-Rhône-Alpes", "FR"),
    ("Dijon", "Bourgogne-Franche-Comté", "FR"),
    ("Angers", "Pays de la Loire", "FR"),
    ("Nîmes", "Occitanie", "FR"),
    ("Villeurbanne", "Auvergne-Rhône-Alpes", "FR"),
    ("Saint-Denis", "Île-de-France", "FR"),
    ("Le Mans", "Pays de la Loire", "FR"),
    ("Aix-en-Provence", "Provence-Alpes-Côte d'Azur", "FR"),
    ("Clermont-Ferrand", "Auvergne-Rhône-Alpes", "FR"),
    ("Brest", "Brittany", "FR"),
    ("Limoges", "Nouvelle-Aquitaine", "FR"),
    ("Tours", "Centre-Val de Loire", "FR"),
    ("Amiens", "Hauts-de-France", "FR"),
    ("Perpignan", "Occitanie", "FR"),
    ("Metz", "Grand Est", "FR"),
    ("Besançon", "Bourgogne-Franche-Comté", "FR"),
    ("Orléans", "Centre-Val de Loire", "FR"),
    ("Mulhouse", "Grand Est", "FR"),
    ("Rouen", "Normandy", "FR"),
    ("Caen", "Normandy", "FR"),
    ("Boulogne-Billancourt", "Île-de-France", "FR"),
    ("Nancy", "Grand Est", "FR"),
    ("Argenteuil", "Île-de-France", "FR"),
    ("Montreuil", "Île-de-France", "FR"),
    ("Saint-Denis", "Réunion", "FR"),
    ("Roubaix", "Hauts-de-France", "FR"),
    ("Tourcoing", "Hauts-de-France", "FR"),
    ("Nanterre", "Île-de-France", "FR"),
    ("Avignon", "Provence-Alpes-Côte d'Azur", "FR"),
    ("Vitry-sur-Seine", "Île-de-France", "FR"),
    ("Créteil", "Île-de-France", "FR"),
    ("Dunkerque", "Hauts-de-France", "FR"),
    ("Poitiers", "Nouvelle-Aquitaine", "FR"),
    ("Courbevoie", "Île-de-France", "FR"),
    ("Versailles", "Île-de-France", "FR"),
    ("Colombes", "Île-de-France", "FR"),
    ("Asnières-sur-Seine", "Île-de-France", "FR"),
    ("Saint-Paul", "Réunion", "FR"),
    ("Rueil-Malmaison", "Île-de-France", "FR"),
    ("Aubervilliers", "Île-de-France", "FR"),
    ("Champigny-sur-Marne", "Île-de-France", "FR"),
    ("Saint-Pierre", "Réunion", "FR"),
    ("Antibes", "Provence-Alpes-Côte d'Azur", "FR"),
    ("Béziers", "Occitanie", "FR"),
    ("La Rochelle", "Nouvelle-Aquitaine", "FR"),
    ("Cannes", "Provence-Alpes-Côte d'Azur", "FR"),
    ("Calais", "Hauts-de-France", "FR"),
    ("Drancy", "Île-de-France", "FR"),
    ("Ajaccio", "Corsica", "FR"),
    ("Mérignac", "Nouvelle-Aquitaine", "FR"),
    ("Bourges", "Centre-Val de Loire", "FR"),
    ("Nanterre", "Île-de-France", "FR"),
    ("Vénissieux", "Auvergne-Rhône-Alpes", "FR"),
    ("Beauvais", "Hauts-de-France", "FR"),
    ("Cergy", "Île-de-France", "FR"),
    ("Pau", "Nouvelle-Aquitaine", "FR"),
    ("Cholet", "Pays de la Loire", "FR"),
    ("Cayenne", "French Guiana", "FR"),
    ("Saint-André", "Réunion", "FR"),
    ("Évry", "Île-de-France", "FR"),
    ("La Seyne-sur-Mer", "Provence-Alpes-Côte d'Azur", "FR"),
    ("Issy-les-Moulineaux", "Île-de-France", "FR"),
    ("Hyères", "Provence-Alpes-Côte d'Azur", "FR"),
    ("Ivry-sur-Seine", "Île-de-France", "FR"),
    ("Levallois-Perret", "Île-de-France", "FR"),
    ("Chambéry", "Auvergne-Rhône-Alpes", "FR"),
    ("Neuilly-sur-Seine", "Île-de-France", "FR"),
    ("Antony", "Île-de-France", "FR"),
    ("Troyes", "Grand Est", "FR"),
    ("Saint-Quentin", "Hauts-de-France", "FR"),
    ("Noisy-le-Grand", "Île-de-France", "FR"),
    ("Villejuif", "Île-de-France", "FR"),
    ("Sarcelles", "Île-de-France", "FR"),
    ("Pessac", "Nouvelle-Aquitaine", "FR"),
    ("Ivry-sur-Seine", "Île-de-France", "FR"),
    ("Épinay-sur-Seine", "Île-de-France", "FR"),
    ("Bondy", "Île-de-France", "FR"),
    ("Chelles", "Île-de-France", "FR"),
    ("Châteauroux", "Centre-Val de Loire", "FR"),
    ("Châtillon", "Île-de-France", "FR"),
    ("Sète", "Occitanie", "FR"),
    ("Saint-Brieuc", "Brittany", "FR"),
    ("Clichy", "Île-de-France", "FR"),
    ("Le Blanc-Mesnil", "Île-de-France", "FR"),
    ("Maisons-Alfort", "Île-de-France", "FR"),
    ("Albi", "Occitanie", "FR"),
]

# Sort the towns based on their size (here just a static list)
# You might want to use actual population data for a dynamic sorting
french_towns = sorted(towns, key=lambda x: unicodedata.normalize('NFKD', x[1]+x[0]).encode('ASCII', 'ignore'))
for town in french_towns:
    print(town)
print (len(french_towns))


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
    
insert_into_location_table(french_towns)