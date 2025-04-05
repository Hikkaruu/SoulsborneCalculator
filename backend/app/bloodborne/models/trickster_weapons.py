from app.database import Base
from sqlalchemy import Column, Integer, String, Float, UniqueConstraint, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

class TricksterWeapons(Base):
    __tablename__ = 'trickster_weapons'
    __table_args__ = (
        UniqueConstraint('name', name='unique_weapon_name'), 
        CheckConstraint('upgrade_lvl >= 0 AND upgrade_lvl <= 10', name='check_upgrade_lvl'),
        # No negative numbers
        CheckConstraint('physical_atk >= 0', name='check_physical_atk'),
        CheckConstraint('blood_atk >= 0', name='check_blood_atk'),
        CheckConstraint('arcane_atk >= 0', name='check_arcane_atk'),
        CheckConstraint('fire_atk >= 0', name='check_fire_atk'),
        CheckConstraint('bolt_atk >= 0', name='check_bolt_atk'),
        CheckConstraint('bullet_use >= 0', name='check_bullet_use'),
        CheckConstraint('rapid_poison >= 0', name='check_rapid_poison'),
        CheckConstraint('strength_scaling >= 0', name='check_strenght_scaling'),
        CheckConstraint('skill_scaling >= 0', name='check_skill_scaling'),
        CheckConstraint('bloodtinge_scaling >= 0', name='check_bloodtinge_scaling'),
        CheckConstraint('arcane_scaling >= 0', name='check_arcane_scaling'),
        CheckConstraint('hp_regain >= 0', name='check_hp_regain'),
        CheckConstraint('strenght_req >= 0', name='check_strenght_req'),
        CheckConstraint('skill_req >= 0', name='check_skill_req'),
        CheckConstraint('bloodtinge_req >= 0', name='check_bloodtinge_req'),
        CheckConstraint('arcane_req >= 0', name='check_arcane_req'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)  
    upgrade_lvl = Column(Integer, nullable=False) 
    name = Column(String, nullable=False)  
    physical_atk = Column(Integer, nullable=False)  
    blood_atk = Column(Integer, nullable=False) 
    arcane_atk = Column(Integer, nullable=False) 
    fire_atk = Column(Integer, nullable=False)  
    bolt_atk = Column(Integer, nullable=False)  
    bullet_use = Column(Integer, nullable=False) 
    rapid_poison = Column(Integer, nullable=False)
    strength_scaling = Column(Float, nullable=False)  
    skill_scaling = Column(Float, nullable=False)  
    bloodtinge_scaling = Column(Float, nullable=False) 
    arcane_scaling = Column(Float, nullable=False)  
    imprints_normal = Column(Integer, nullable=False)  
    imprints_uncanny = Column(Integer, nullable=False)  
    imprints_lost = Column(Integer, nullable=False)  
    hp_regain = Column(Integer, nullable=False)  
    strenght_req = Column(Integer, nullable=False)  
    skill_req = Column(Integer, nullable=False)  
    bloodtinge_req = Column(Integer, nullable=False)  
    arcane_req = Column(Integer, nullable=False)  