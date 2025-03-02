from typing import Union
from fastapi import FastAPI
from .database import Base, engine
from app.bloodborne.models.trickster_weapons import TricksterWeapons
from app.bloodborne.models.firearms import Firearms
from app.seeders import seeder
from app.bloodborne.routers import firearms

app = FastAPI()

#Create tables
Base.metadata.create_all(bind=engine)

seeder.seed_from_excel('app\\seeders\\bloodborne.xlsx', "Use_TricksterWeapons", TricksterWeapons)
seeder.seed_from_excel('app\\seeders\\bloodborne.xlsx', "Use_Firearms", Firearms)

app.include_router(firearms.router)