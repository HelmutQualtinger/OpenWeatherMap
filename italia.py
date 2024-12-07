# Lista di tuple contenenti il nome della città e la regione
citta_italiane = [
    ("Roma", "Lazio", "IT"),
    ("Milano", "Lombardia", "IT"),
    ("Napoli", "Campania", "IT"),
    ("Torino", "Piemonte", "IT"),
    ("Palermo", "Sicilia", "IT"),
    ("Genova", "Liguria", "IT"),
    ("Bologna", "Emilia-Romagna", "IT"),
    ("Firenze", "Toscana", "IT"),
    ("Bari", "Puglia", "IT"),
    ("Catania", "Sicilia", "IT"),
    ("Venezia", "Veneto", "IT"),
    ("Verona", "Veneto", "IT"),
    ("Messina", "Sicilia", "IT"),
    ("Padova", "Veneto", "IT"),
    ("Trieste", "Friuli-Venezia Giulia", "IT"),
    ("Brescia", "Lombardia", "IT"),
    ("Taranto", "Puglia", "IT"),
    ("Prato", "Toscana", "IT"),
    ("Reggio Calabria", "Calabria", "IT"),
    ("Modena", "Emilia-Romagna", "IT"),
    ("Reggio Emilia", "Emilia-Romagna", "IT"),
    ("Perugia", "Umbria", "IT"),
    ("Livorno", "Toscana", "IT"),
    ("Ravenna", "Emilia-Romagna", "IT"),
    ("Cagliari", "Sardegna", "IT"),
    ("Foggia", "Puglia", "IT"),
    ("Rimini", "Emilia-Romagna", "IT"),
    ("Salerno", "Campania", "IT"),
    ("Ferrara", "Emilia-Romagna", "IT"),
    ("Sassari", "Sardegna", "IT"),
    ("Latina", "Lazio", "IT"),
    ("Giugliano in Campania", "Campania", "IT"),
    ("Monza", "Lombardia", "IT"),
    ("Siracusa", "Sicilia", "IT"),
    ("Pescara", "Abruzzo", "IT"),
    ("Bergamo", "Lombardia", "IT"),
    ("Forlì", "Emilia-Romagna", "IT"),
    ("Trento", "Trentino-Alto Adige", "IT"),
    ("Vicenza", "Veneto", "IT"),
    ("Terni", "Umbria", "IT"),
    ("Bolzano", "Trentino-Alto Adige", "IT"),
    ("Novara", "Piemonte", "IT"),
    ("Barletta", "Puglia", "IT"),
    ("Como", "Lombardia", "IT"),
    ("Piacenza", "Emilia-Romagna", "IT"),
    ("Andria", "Puglia", "IT"),
    ("Cesena", "Emilia-Romagna", "IT"),
    ("Lecce", "Puglia", "IT"),
    ("Pesaro", "Marche", "IT"),
    ("Alessandria", "Piemonte", "IT"),
    ("La Spezia", "Liguria", "IT"),
    ("Grosseto", "Toscana", "IT"),
    ("Cremona", "Lombardia", "IT"),
    ("Lucca", "Toscana", "IT"),
    ("Varese", "Lombardia", "IT"),
    ("Sesto San Giovanni", "Lombardia", "IT"),
    ("Potenza", "Basilicata", "IT"),
    ("Arezzo", "Toscana", "IT"),
    ("Cinisello Balsamo", "Lombardia", "IT"),
    ("Marsala", "Sicilia", "IT"),
    ("Ragusa", "Sicilia", "IT"),
    ("Asti", "Piemonte", "IT"),
    ("Viterbo", "Lazio", "IT"),
    ("Fano", "Marche", "IT"),
    ("Trapani", "Sicilia", "IT"),
    ("Foligno", "Umbria", "IT"),
    ("Cosenza", "Calabria", "IT"),
    ("Lodi", "Lombardia", "IT"),
    ("Imola", "Emilia-Romagna", "IT"),
    ("Carrara", "Toscana", "IT"),
    ("Biella", "Piemonte", "IT"),
    ("Lamezia Terme", "Calabria", "IT"),
    ("Aprilia", "Lazio", "IT"),
    ("Altamura", "Puglia", "IT"),
    ("Pordenone", "Friuli-Venezia Giulia", "IT"),
    ("Massa", "Toscana", "IT"),
    ("Savona", "Liguria", "IT"),
    ("Matera", "Basilicata", "IT"),
    ("Agrigento", "Sicilia", "IT"),
    ("Aversa", "Campania", "IT"),
    ("Legnano", "Lombardia", "IT"),
    ("Acerra", "Campania", "IT"),
    ("Castellammare di Stabia", "Campania", "IT"),
    ("Civitavecchia", "Lazio", "IT"),
    ("Pozzuoli", "Campania", "IT"),
    ("Velletri", "Lazio", "IT"),
    ("Rovigo", "Veneto", "IT"),
    ("Vercelli", "Piemonte", "IT"),
    ("Ercolano", "Campania", "IT"),
    ("Rho", "Lombardia", "IT"),
    ("Pomezia", "Lazio", "IT"),
    ("Cava de' Tirreni", "Campania", "IT")
]

citta_italiane.sort(key=lambda tupla: (tupla[1],tupla[0]))
# Stampa tutte le città italiane con le rispettive regioni
for indice, (citta, regione,_) in enumerate(citta_italiane):
    print(f"{indice}. {citta} - {regione}")
    

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
    
insert_into_location_table(citta_italiane)
