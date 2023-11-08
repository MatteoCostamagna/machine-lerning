from pydantic import BaseModel

class Data(BaseModel):
    id: int
    fixed_acidity:int 
    volatile_acidity:int 
    citric_acid:int 
    residual_sugar:int 
    chlorides:int 
    free_sulfur_dioxide:int 
    total_sulfur_dioxide:int 
    density:int 
    pH:int 
    sulphates:int 
    alcohol:int 
    quality:int
    red_or_white:int