from models.operation import Operation
from models.operation_item import OperationItem
from models.stock import Stock
from models.stock_movement import StockMovement


def create_receipt(db, receipt_data):
    operation = Operation(
        type="receipt",
        status="done",
        destination_warehouse=receipt_data.destination_warehouse
    )

    db.add(operation)
    db.commit()
    db.refresh(operation)

    for item in receipt_data.items:
        operation_item = OperationItem(
            operation_id=operation.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(operation_item)

        stock = db.query(Stock).filter(
            Stock.product_id == item.product_id,
            Stock.warehouse_id == receipt_data.destination_warehouse
        ).first()

        if not stock:
            stock = Stock(
                product_id=item.product_id,
                warehouse_id=receipt_data.destination_warehouse,
                quantity=0
            )
            db.add(stock)

        stock.quantity += item.quantity

        movement = StockMovement(
            product_id=item.product_id,
            warehouse_id=receipt_data.destination_warehouse,
            operation_id=operation.id,
            movement_type="IN",
            quantity=item.quantity
        )

        db.add(movement)

    db.commit()

    return {"message": "Receipt created and stock updated"}