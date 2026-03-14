from models.operation import Operation
from models.operation_item import OperationItem
from models.stock import Stock
from models.stock_movement import StockMovement

def create_transfer(db, transfer_data):

    operation = Operation(
        type="transfer",
        status="done",
        source_warehouse=transfer_data.source_warehouse,
        destination_warehouse=transfer_data.destination_warehouse
    )

    db.add(operation)
    db.commit()
    db.refresh(operation)

    for item in transfer_data.items:

        source_stock = db.query(Stock).filter(
            Stock.product_id == item.product_id,
            Stock.warehouse_id == transfer_data.source_warehouse
        ).first()

        if not source_stock or source_stock.quantity < item.quantity:
            raise Exception("Not enough stock to transfer")

        source_stock.quantity -= item.quantity

        destination_stock = db.query(Stock).filter(
            Stock.product_id == item.product_id,
            Stock.warehouse_id == transfer_data.destination_warehouse
        ).first()

        if not destination_stock:
            destination_stock = Stock(
                product_id=item.product_id,
                warehouse_id=transfer_data.destination_warehouse,
                quantity=0
            )
            db.add(destination_stock)

        destination_stock.quantity += item.quantity

        operation_item = OperationItem(
            operation_id=operation.id,
            product_id=item.product_id,
            quantity=item.quantity
        )

        db.add(operation_item)

        movement_out = StockMovement(
            product_id=item.product_id,
            warehouse_id=transfer_data.source_warehouse,
            operation_id=operation.id,
            movement_type="TRANSFER_OUT",
            quantity=item.quantity
        )

        movement_in = StockMovement(
            product_id=item.product_id,
            warehouse_id=transfer_data.destination_warehouse,
            operation_id=operation.id,
            movement_type="TRANSFER_IN",
            quantity=item.quantity
        )

        db.add(movement_out)
        db.add(movement_in)

    db.commit()

    return {"message": "Transfer completed"}



# 1 Check stock in source warehouse
# 2 Reduce stock from source
# 3 Increase stock in destination
# 4 Log transfer movements