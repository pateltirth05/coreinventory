from models.operation import Operation
from models.operation_item import OperationItem
from models.stock import Stock
from models.stock_movement import StockMovement


def create_delivery(db, delivery_data):

    operation = Operation(
        type="delivery",
        status="done",
        source_warehouse=delivery_data.source_warehouse
    )

    db.add(operation)
    db.commit()
    db.refresh(operation)

    for item in delivery_data.items:

        stock = db.query(Stock).filter(
            Stock.product_id == item.product_id,
            Stock.warehouse_id == delivery_data.source_warehouse
        ).first()

        if not stock or stock.quantity < item.quantity:
            raise Exception("Not enough stock available")

        stock.quantity -= item.quantity

        operation_item = OperationItem(
            operation_id=operation.id,
            product_id=item.product_id,
            quantity=item.quantity
        )

        db.add(operation_item)

        movement = StockMovement(
            product_id=item.product_id,
            warehouse_id=delivery_data.source_warehouse,
            operation_id=operation.id,
            movement_type="OUT",
            quantity=item.quantity
        )

        db.add(movement)

    db.commit()

    return {"message": "Delivery completed"}