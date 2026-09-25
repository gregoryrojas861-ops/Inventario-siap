from database.database import init_db,SessionLocal
from database.models import User,Material
from services.inventory_service import create_material
from utils.security import hash_password

def test_material_creation():
    init_db(); db=SessionLocal(); u=User(username="pytest_user",full_name="Test",password_hash=hash_password("Test1234!"),role="ADMINISTRADOR"); db.add(u); db.commit();
    m=create_material(db,u,{"code":"PYTEST-1","name":"Material Test","stock":10,"cost":2,"min_stock":1,"max_stock":20,"safety_stock":1,"reorder_point":2,"criticality":"MEDIA","category":"Test","unit":"unidad"}); assert m.stock==10; db.close()
