# uvicorn Database.main:app --reload --> x avviare le api
# http://127.0.0.1:8000/docs. Swagger


from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
 
app = FastAPI()

#Ho creato una classe utile per le api
class Data(BaseModel):
    fixed_acidity:float 
    volatile_acidity:float 
    citric_acid:float 
    residual_sugar:float 
    chlorides:float 
    free_sulfur_dioxide:float 
    density:float 
    pH:float 
    sulphates:float 
    alcohol:float 
    quality:int
    tow: int 
    top_quality:int


#create 

@app.post("/data")
def create_data(data : Data):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("INSERT INTO data (fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,free_sulfur_dioxide, density, pH, sulphates, alcohol, quality, tow, top_quality)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (data.fixed_acidity, data.volatile_acidity, data.citric_acid, data.residual_sugar, data.chlorides,data.free_sulfur_dioxide, data.density, data.pH, data.sulphates, data.alcohol, data.quality, data.tow, data.best_quality))
  result = cursor.fetchall()
  conn.commit()
  conn.close()
  return {"message": "Wine successfully created"}

#read

@app.get("/data")
def read_all_datas():
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM data")
  result = cursor.fetchall()
  conn.commit()
  conn.close()
  return result

@app.get("/data/{quality}")
def data_by_quality(quality: int):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM data WHERE quality = ?",(quality,))
  result = cursor.fetchall()
  conn.commit()
  conn.close()
  return result

@app.get("/data/{alcohol}")
def data_by_tow(alcohol: float):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM data WHERE alcohol = ?",(alcohol,))
  result = cursor.fetchall()
  conn.commit()
  conn.close()
  return result

#update

@app.put("/data")
def update_data(data : Data):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("UPDATE wine SET fixed_acidity=?, volatile_acidity=?, citric_acid=?, residual_sugar=?, chlorides=?, free_sulfur_dioxide=?, density=?, pH=?, sulphates=?, alcohol=?, quality=?, tow=?, top_quality=? WHERE fixed_acidity=? AND volatile_acidity=? AND citric_acid=? AND residual_sugar=? AND chlorides=? AND free_sulfur_dioxide=? AND density=? AND pH=? AND sulphates=? AND alcohol=? AND quality=? AND tow=? AND top_quality=?", (data.fixed_acidity, data.volatile_acidity, data.citric_acid, data.residual_sugar, data.chlorides, data.free_sulfur_dioxide, data.density, data.pH, data.sulphates, data.alcohol, data.quality, data.tow, data.top_quality, data.fixed_acidity, data.volatile_acidity, data.citric_acid, data.residual_sugar, data.chlorides, data.free_sulfur_dioxide, data.density, data.pH, data.sulphates, data.alcohol, data.quality, data.tow, data.top_quality))
  conn.commit()
  conn.close()
  return {}


#delete

@app.delete("/data")
def delete_data_all(data : Data):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE * FROM data")
    conn.commit()
    conn.close()
    return {}

"""
@app.delete("/data/{id}")
def delete_data_byid(id: int):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM data where id= ?",(id,))
    conn.commit()
    conn.close()
    return {}
  
"""