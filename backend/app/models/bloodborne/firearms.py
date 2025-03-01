from app.database import Base
from sqlalchemy import Column, Integer, String, Float, UniqueConstraint, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

class Firearms(Base):
    __tablename__ = 'firearms'
    __table_args__ = (
        UniqueConstraint('name', name='unique_firearm_name'),  
        CheckConstraint('upgrade_lvl >= 0 AND upgrade_lvl <= 10', name='check_upgrade_lvl'),  
        CheckConstraint('physical_atk >= 0', name='check_physical_atk'),
        CheckConstraint('blood_atk >= 0', name='check_blood_atk'),
        CheckConstraint('arcane_atk >= 0', name='check_arcane_atk'),
        CheckConstraint('fire_atk >= 0', name='check_fire_atk'),
        CheckConstraint('bolt_atk >= 0', name='check_bolt_atk'),
        CheckConstraint('bullet_use >= 0', name='check_bullet_use'),
        CheckConstraint('strength_scaling >= 0', name='check_strength_scaling'),
        CheckConstraint('skill_scaling >= 0', name='check_skill_scaling'),
        CheckConstraint('bloodtinge_scaling >= 0', name='check_bloodtinge_scaling'),
        CheckConstraint('arcane_scaling >= 0', name='check_arcane_scaling'),
        CheckConstraint('strenght_req >= 0', name='check_strenght_req'),
        CheckConstraint('socket >= 0', name='socket'),
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
    strength_scaling = Column(Float, nullable=False)  
    skill_scaling = Column(Float, nullable=False)  
    bloodtinge_scaling = Column(Float, nullable=False)  
    arcane_scaling = Column(Float, nullable=False)  
    socket = Column(Integer, nullable=False)  
    strenght_req = Column(Integer, nullable=False)  
    skill_req = Column(Integer, nullable=False)  
    bloodtinge_req = Column(Integer, nullable=False) 
    arcane_req = Column(Integer, nullable=False)  