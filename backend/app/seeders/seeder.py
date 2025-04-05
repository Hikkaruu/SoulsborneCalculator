import pandas as pd
from sqlalchemy.orm import Session
from app.database import SessionLocal

def seed_from_excel(file_path: str, sheet_name: str, db_model: Session = None):
    df = None
    
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df = df.fillna(0)
    except Exception as e:
        print(f"Error loading Excel sheet: {e}")
        return
    
    # connect to DB
    db = SessionLocal()

    try:
        if db.query(db_model).count() == 0:
            # Excel data to dict
            weapons_data = df.to_dict(orient="records")

            # Add data to database
            for weapon_data in weapons_data:
                weapon = db_model(**weapon_data)
                db.add(weapon)
            db.commit()
            print("Seeding completed successfully.")
            print("----------------------------------------------------")
            print(f"Excel sheet {sheet_name} Loaded Successfuly:")
            print(df)
            print("----------------------------------------------------")
        else:
            print("Table already seeded.")
    except Exception as e:
        db.rollback()
        print(f"Seeding error: {e}")
        return
    finally:
        db.close()