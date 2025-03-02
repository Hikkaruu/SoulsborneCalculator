from sqlalchemy.orm import Session
from ..models.firearms import Firearms
from ..schemas.firearms import FirearmCreate, FirearmUpdate

class FirearmService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_firearms(self):
        return self.db.query(Firearms).all()

    def get_firearm_by_id(self, firearm_id: int):
        return self.db.query(Firearms).filter(Firearms.id == firearm_id).first()
    
    def get_firearm_by_name(self, name: str):
        return self.db.query(Firearms).filter(Firearms.name == name).first()
    
    def get_all_firearms_by_upgrade_lvl(self, upgrade_lvl: int):
        return self.db.query(Firearms).filter(Firearms.upgrade_lvl == upgrade_lvl).all()
    
    def can_wield_firearm(self, firearm_id: int, strength: int, skill: int, bloodtinge: int, arcane: int):
        return self.db.query(Firearms).filter(Firearms.strenght_req <= strength, Firearms.skill_req <= skill, Firearms.bloodtinge_req <= bloodtinge, Firearms.arcane_req <= arcane).first()
    
    def get_all_wieldable_firearms(self, strength: int, skill: int, bloodtinge: int, arcane: int):
        return self.db.query(Firearms).filter(Firearms.strenght_req <= strength, Firearms.skill_req <= skill, Firearms.bloodtinge_req <= bloodtinge, Firearms.arcane_req <= arcane).all()

    def create_firearm(self, firearm: FirearmCreate):
        db_firearm = Firearms(**firearm.model_dump())
        self.db.add(db_firearm)
        self.db.commit()
        self.db.refresh(db_firearm)
        return db_firearm

    def update_firearm(self, firearm_id: int, firearm: FirearmUpdate):
        try:
            db_firearm = self.db.query(Firearms).filter(Firearms.id == firearm_id).first()
            if not db_firearm:
                return None
            for key, value in firearm.model_dump().items():
                setattr(db_firearm, key, value)
            self.db.commit()
            self.db.refresh(db_firearm)
            return db_firearm
        except Exception as e:
            print(f"Error while trying to Update: {e}")

    def delete_firearm(self, firearm_id: int):
        db_firearm = self.db.query(Firearms).filter(Firearms.id == firearm_id).first()
        if not db_firearm:
            return False
        self.db.delete(db_firearm)
        self.db.commit()
        return True