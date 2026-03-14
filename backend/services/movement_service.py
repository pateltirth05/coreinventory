from models.stock_movement import StockMovement


def get_movements(db):

    movements = db.query(StockMovement).all()

    result = []

    for m in movements:
        result.append({
            "id": m.id,
            "product_id": m.product_id,
            "warehouse_id": m.warehouse_id,
            "operation_id": m.operation_id,
            "movement_type": m.movement_type,
            "quantity": m.quantity,
            
        })

    return result