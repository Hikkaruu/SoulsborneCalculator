from typing import Union
from fastapi import FastAPI
from .database import Base, engine
from app.models.bloodborne.trickster_weapons import TricksterWeapons
from app.models.bloodborne.firearms import Firearms
from app.seeders import seeder

app = FastAPI()

#Create tables
Base.metadata.create_all(bind=engine)

seeder.seed_from_excel('app\\seeders\\bloodborne.xlsx', "Use_TricksterWeapons", TricksterWeapons)
seeder.seed_from_excel('app\\seeders\\bloodborne.xlsx', "Use_Firearms", Firearms)

@app.get("/")
def read_root():
    return {"SS": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
