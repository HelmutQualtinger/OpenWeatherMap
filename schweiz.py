orte = [
    ("Zürich", "Zürich"),
    ("Genf", "Genf"),
    ("Basel", "Basel-Stadt"),
    ("Bern", "Bern"),
    ("Lausanne", "Waadt"),
    ("Winterthur", "Zürich"),
    ("Luzern", "Luzern"),
    ("St. Gallen", "St. Gallen"),
    ("Lugano", "Tessin"),
    ("Biel/Bienne", "Bern"),
    ("Thun", "Bern"),
    ("Köniz", "Bern"),
    ("La Chaux-de-Fonds", "Neuenburg"),
    ("Schaffhausen", "Schaffhausen"),
    ("Freiburg", "Freiburg"),
    ("Chur", "Graubünden"),
    ("Vernier", "Genf"),
    ("Neuenburg", "Neuenburg"),
    ("Uster", "Zürich"),
    ("Sitten", "Wallis"),
    ("Lancy", "Genf"),
    ("Yverdon-les-Bains", "Waadt"),
    ("Emmen", "Luzern"),
    ("Zug", "Zug"),
    ("Kriens", "Luzern"),
    ("Rapperswil-Jona", "St. Gallen"),
    ("Dübendorf", "Zürich"),
    ("Dietikon", "Zürich"),
    ("Montreux", "Waadt"),
    ("Frauenfeld", "Thurgau"),
    ("Wetzikon", "Zürich"),
    ("Wil", "St. Gallen"),
    ("Baar", "Zug"),
    ("Meyrin", "Genf"),
    ("Bulle", "Freiburg"),
    ("Kreuzlingen", "Thurgau"),
    ("Riehen", "Basel-Stadt"),
    ("Renens", "Waadt"),
    ("Nyon", "Waadt"),
    ("Bellinzona", "Tessin"),
    ("Vevey", "Waadt"),
    ("Bülach", "Zürich"),
    ("Aarau", "Aargau"),
    ("Allschwil", "Basel-Landschaft"),
    ("Spreitenbach", "Aargau"),
    ("Volketswil", "Zürich"),
    ("Carouge", "Genf"),
    ("Wädenswil", "Zürich"),
    ("Kloten", "Zürich"),
    ("Pully", "Waadt"),
    ("Thalwil", "Zürich"),
    ("Wettingen", "Aargau"),
    ("Regensdorf", "Zürich"),
    ("Baden", "Aargau"),
    ("Pratteln", "Basel-Landschaft"),
    ("Morges", "Waadt"),
    ("Adliswil", "Zürich"),
    ("Wohlen", "Aargau"),
    ("Muri bei Bern", "Bern"),
    ("Oberwil", "Basel-Landschaft"),
    ("Monthey", "Wallis"),
    ("Zollikon", "Zürich"),
    ("Brig-Glis", "Wallis"),
    ("Horgen", "Zürich"),
    ("Gossau", "St. Gallen"),
    ("Steffisburg", "Bern"),
    ("Horw", "Luzern"),
    ("Locarno", "Tessin"),
    ("Grenchen", "Solothurn"),
    ("Uzwil", "St. Gallen"),
    ("Binningen", "Basel-Landschaft"),
    ("Ebikon", "Luzern"),
    ("Schlieren", "Zürich"),
    ("Aesch", "Basel-Landschaft"),
    ("Muttenz", "Basel-Landschaft"),
    ("Siders", "Wallis"),
    ("Zofingen", "Aargau"),
    ("Pfäffikon", "Zürich"),
    ("Rüti", "Zürich"),
    ("Arbon", "Thurgau"),
    ("Weinfelden", "Thurgau"),
    ("Altstätten", "St. Gallen"),
    ("Brugg", "Aargau"),
    ("Bassersdorf", "Zürich"),
    ("Ittigen", "Bern"),
    ("Zollikofen", "Bern"),
    ("Olten", "Solothurn"),
    ("Küsnacht", "Zürich"),
    ("Gland", "Waadt"),
    ("Cham", "Zug"),
    ("Meilen", "Zürich"),
    ("Amriswil", "Thurgau"),
    ("Veyrier", "Genf"),
    ("Worb", "Bern"),
    ("Romanshorn", "Thurgau"),
    ("Möhlin", "Aargau"),
    ("Münchenstein", "Basel-Landschaft")
]

# Alphabetically sorting the list based on city names
orte.sort(key=lambda x: x[0])

print(orte)