import pandas as pd
import sqlite3

# Creazione di una connessione al database (o lo crea se non esiste)
conn = sqlite3.connect('database.db')

# Creazione di un cursore per eseguire comandi SQL
cursor = conn.cursor()


# Creazione della tabella "vino_rosso"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY,
        fixed_acidity INTEGER,
        volatile_acidity INTEGER,
        citric_acid INTEGER,
        residual_sugar INTEGER,
        chlorides INTEGER,
        free_sulfur_dioxide INTEGER, 
        total_sulfur_dioxide INTEGER,
        density INTEGER,
        pH INTEGER,
        sulphates INTEGER,
        alcohol INTEGER,
        quality INTEGER,
        red_or_white INTEGER
    )
''')


# Salvataggio delle modifiche e chiusura del cursore e della connessione
conn.commit()
cursor.close()
conn.close()


df_vino_rosso = pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/wine_quality/winequality-red.csv', sep=';', encoding='latin1')
df_vino_bianco = pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/wine_quality/winequality-red.csv', sep=';', encoding='latin1')

print(df_vino_bianco)
print(df_vino_rosso)



conn = sqlite3.connect('database.db')
df_vino_bianco.to_sql('data', conn, if_exists='replace', index=False)

