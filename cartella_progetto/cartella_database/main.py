from fastapi import FastAPI
from pydantic import BaseModel
from crud import *
 
app = FastAPI()

#create

@app.post("/data")
def create_data(data : Data):
    data_id = create_data(data)
    return {"id": data_id, **data.model_dump()}

#read

@app.get("/data")
def read_all_datas():
   return read_all_datas()

@app.get("/data/{regione}")
def data_by_regione(regione: str):
  return read_data_by_regione(regione)

@app.get("/data/{anno}")
def data_by_anno(anno: int):
  return read_data_by_anno(anno)

#update

"""
@app.post("/data")
def create_data(data : Data):
    data_id = create_data(data)
    return {"id": data_id, **data.model_dump()}

"""

#delete

@app.delete("/data")
def delete_data_all(data : Data):
    data_id = delete_data(data)
    return {}

@app.delete("/data/{id}")
def delete_data_byid(id: int):
    data_id = delete_data_by_id(id)
    return {"id" : data_id}
