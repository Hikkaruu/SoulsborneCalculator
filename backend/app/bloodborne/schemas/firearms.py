from pydantic import BaseModel

class FirearmBase(BaseModel):
    upgrade_lvl: int
    name: str
    physical_atk: int
    blood_atk: int
    arcane_atk: int
    fire_atk: int
    bolt_atk: int
    bullet_use: int
    strength_scaling: float
    skill_scaling: float
    bloodtinge_scaling: float
    arcane_scaling: float
    socket: int
    strenght_req: int
    skill_req: int
    bloodtinge_req: int
    arcane_req: int

class FirearmCreate(FirearmBase):
    pass

class FirearmUpdate(FirearmBase):
    pass

class Firearm(FirearmBase):
    id: int

    class Config:
        from_attributes = True