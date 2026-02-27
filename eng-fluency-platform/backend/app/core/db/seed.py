import json
import os
from sqlalchemy.orm import Session
from app.core.db.session import SessionLocal
from app.models.linguistics import Cognate
from app.models.tenant import Tenant

def seed_data():
    db: Session = SessionLocal()
    try:
        # Create a default tenant if not exists
        default_tenant = db.query(Tenant).filter(Tenant.slug == "default").first()
        if not default_tenant:
            default_tenant = Tenant(name="Default Tenant", slug="default")
            db.add(default_tenant)
            db.commit()
            db.refresh(default_tenant)
        
        # Load cognates
        data_path = os.path.join(os.path.dirname(__file__), "seed_cognates.json")
        with open(data_path, 'r', encoding='utf-8') as f:
            cognates_data = json.load(f)
        
        for item in cognates_data:
            exists = db.query(Cognate).filter(
                Cognate.english_word == item["english_word"],
                Cognate.tenant_id == default_tenant.id
            ).first()
            if not exists:
                cognate = Cognate(**item, tenant_id=default_tenant.id)
                db.add(cognate)
        
        db.commit()
        print(f"Successfully seeded {len(cognates_data)} cognates for tenant: {default_tenant.slug}")
    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
