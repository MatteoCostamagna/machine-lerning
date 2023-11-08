from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from model import *

app = FastAPI()


def create_data(data: Data):
 conn = sqlite3.connect('database.db')
 cursor = conn.cursor()
 cursor.execute("INSERT INTO data(id, regione, anno, arrivi, presenze) VALUES (?,?,?,?,?)", (data.id, data.regione, data.anno, data.arrivi, data.presenze))
 conn.commit()
 conn.close()


def read_all_datas():
 conn = sqlite3.connect('database.db')
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM data")
 result = cursor.fetchall()
 conn.commit()
 conn.close()
 return result

def read_data_by_quality(quality:int):
 conn = sqlite3.connect('database.db')
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM data where quality= ?",(quality,))
 result = cursor.fetchall()
 conn.commit()
 conn.close()
 return result

def read_data_by_regione(regione:str):
 conn = sqlite3.connect('database.db')
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM data where regione= ?",(regione,))
 result = cursor.fetchall()
 conn.commit()
 conn.close()
 return result


def delete_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE * FROM data")
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result


def delete_data_by_id(id: int):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM data where id= ?",(id,))
    conn.commit()
    conn.close()
    return {"message": f"Dato con ID {id} eliminato con successo"}

