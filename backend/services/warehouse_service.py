from models.warehouse import Warehouse
# Handles database operations.
def create_warehouse(db, warehouse_data):
    warehouse = Warehouse(**warehouse_data.dict())
    db.add(warehouse)
    db.commit()
    db.refresh(warehouse)
    return warehouse


def get_warehouses(db):
    return db.query(Warehouse).all()