from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.firearms import Firearm, FirearmCreate, FirearmUpdate
from ..services.firearms import FirearmService
from ...database import SessionLocal

router = APIRouter(prefix="/firearms", tags=["firearms"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Firearm])
def get_all_firearms(db: Session = Depends(get_db)):
    service = FirearmService(db)
    return service.get_all_firearms()

@router.get("/id/{firearm_id}", response_model=Firearm)
def get_firearm(firearm_id: int, db: Session = Depends(get_db)):
    service = FirearmService(db)
    firearm = service.get_firearm_by_id(firearm_id)
    if not firearm:
        raise HTTPException(status_code=404, detail=f"Firearm with id:{firearm_id} not found")
    return firearm

@router.get("/name/{name}", response_model=Firearm)
def get_firearm_by_name(name: str, db: Session = Depends(get_db)):
    service = FirearmService(db)
    firearm = service.get_firearm_by_name(name)
    if not firearm:
        raise HTTPException(status_code=404, detail=f"Firearm named:{name} not found")
    return firearm

@router.get("/upgrade_lvl/{upgrade_lvl}", response_model=list[Firearm])
def get_all_firearms_by_upgrade_lvl(upgrade_lvl: int, db: Session = Depends(get_db)):
    service = FirearmService(db)
    if upgrade_lvl < 0 or upgrade_lvl > 10:
        raise HTTPException(status_code=400, detail="Upgrade level must be <0, 10>")
    return service.get_all_firearms_by_upgrade_lvl(upgrade_lvl)

@router.get("/can_wield/{firearm_id}")
def can_wield_firearm(firearm_id: int, strength: int, skill: int, bloodtinge: int, arcane: int, db: Session = Depends(get_db)):
    service = FirearmService(db)
    if not service.can_wield_firearm(firearm_id, strength, skill, bloodtinge, arcane):
        return False
    return True

@router.get("/wieldable_firearms")
def get_all_wieldable_firearms(strength: int, skill: int, bloodtinge: int, arcane: int, db: Session = Depends(get_db)):
    service = FirearmService(db)
    return service.get_all_wieldable_firearms(strength, skill, bloodtinge, arcane)

@router.post("/", response_model=Firearm)
def create_firearm(firearm: FirearmCreate, db: Session = Depends(get_db)):
    service = FirearmService(db)
    return service.create_firearm(firearm)

# Zaktualizuj rekord broni palnej
@router.put("/{firearm_id}", response_model=Firearm)
def update_firearm(firearm_id: int, firearm: FirearmUpdate, db: Session = Depends(get_db)):
    service = FirearmService(db)
    updated_firearm = service.update_firearm(firearm_id, firearm)
    if not updated_firearm:
        raise HTTPException(status_code=404, detail=f"Firearm with id:{firearm_id} not found")
    return updated_firearm

# Usuń rekord broni palnej
@router.delete("/{firearm_id}")
def delete_firearm(firearm_id: int, db: Session = Depends(get_db)):
    service = FirearmService(db)
    if not service.delete_firearm(firearm_id):
        raise HTTPException(status_code=404, detail=f"Firearm with id:{firearm_id} not found")
    return {"message": "Firearm deleted"}