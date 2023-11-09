import pandas as pd
import sqlite3

# Creazione di una connessione al database (o lo crea se non esiste)
conn = sqlite3.connect('database.db')

# Creazione di un cursore per eseguire comandi SQL
cursor = conn.cursor()


# Creazione della tabella "data" --> che contiene i dati del vino
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        fixed_acidity FLOAT,
        volatile_acidity FLOAT,
        citric_acid FLOAT,
        residual_sugar FLOAT,
        chlorides FLOAT,
        free_sulfur_dioxide FLOAT,
        density FLOAT,
        pH FLOAT,
        sulphates FLOAT,
        alcohol FLOAT,
        quality INTEGER,
        tow INTEGER,
        top_quality INTEGER
    )
''')


# Salvataggio delle modifiche e chiusura del cursore e della connessione
conn.commit()
cursor.close()
conn.close()

#Ho letto il file dei vini che viene salvato nella cartella training
df_vino = pd.read_csv('https://raw.githubusercontent.com/MatteoCostamagna/machine-lerning/main/cartella_progetto/cartella_training/vino.csv', sep=',', encoding='latin1')
#print(df_vino)

conn = sqlite3.connect('database.db')
#Ho caricato i dati nella tabella precedentemente creata
df_vino.to_sql('data', conn, if_exists='replace', index=False)

