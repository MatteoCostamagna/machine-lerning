from pydantic import BaseModel

class Data(BaseModel):
    id: int
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
    tow:int
    best_quality:int