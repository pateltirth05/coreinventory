from models.operation import Operation
from models.operation_item import OperationItem
from models.stock import Stock
from models.stock_movement import StockMovement


def create_adjustment(db, adjustment_data):

    operation = Operation(
        type="adjustment",
        status="done"
    )

    db.add(operation)
    db.commit()
    db.refresh(operation)

    for item in adjustment_data.items:

        stock = db.query(Stock).filter(
            Stock.product_id == item.product_id,
            Stock.warehouse_id == item.warehouse_id
        ).first()

        if not stock:
            raise Exception("Stock record not found")

        difference = item.counted_quantity - stock.quantity

        stock.quantity = item.counted_quantity

        operation_item = OperationItem(
            operation_id=operation.id,
            product_id=item.product_id,
            quantity=difference
        )

        db.add(operation_item)

        movement = StockMovement(
            product_id=item.product_id,
            warehouse_id=item.warehouse_id,
            operation_id=operation.id,
            movement_type="ADJUSTMENT",
            quantity=difference
        )

        db.add(movement)

    db.commit()

    return {"message": "Inventory adjusted"}