from fastapi import FastAPI , Request
from pydantic import BaseModel
from sqlalchemy import create_engine, text 
from functools import wraps
import os

app = FastAPI()

def get_db():
    DATABASE = os.path.join(".", "people.db")
    db = create_engine("sqlite:///" + DATABASE)
    return db 
    
class NotFound(Exception):
    pass
    
class person(BaseModel):
    name : str
    age : int
    
class person_search(BaseModel):
    name : str    
    
def get_age(name):
    eng = get_db()
    with eng.connect() as conn:
        res = conn.execute(text("select age from people where name = :name"),dict(name=name)).fetchone()
        if res:
            return sum(res)
        else:
            raise NotFound("NotFound")
                
                        
def post_age(name, age):
    eng = get_db()
    with eng.connect() as conn:
        res = conn.execute(
                text("INSERT INTO people (name, age) VALUES (:name, :age)"),
                {"name": name, "age": age})
        conn.commit()        
        return res       
                
    
@app.get("/helloj")
@app.get("/helloj/{fname}")
@app.get("/hello/{fname}/{format}")
def get_data(fname = None, name: str = None, format: str = "json", jsonname: person_search= None):
    try:
        actual_name = fname or name or (jsonname.name if jsonname else "Raviteja")
        if format == "json":
            age = get_age(actual_name)
            return {"name": actual_name, "age": age}
        else:
            return {"Error":"parsing"}
    except NotFound:
        return {"Error":"Not found"}

    
         
@app.post("/helloj")
def post_person(person_:person):
    if person_.name and person_.age:
        res = post_age(person_.name,person_.age)
        if res:
            return {"Inserted":"Successfully"}
        
    


