from sqlalchemy import func
from models.stock import Stock
from models.product import Product
from models.operation import Operation


def get_dashboard_data(db):

    total_stock = db.query(func.sum(Stock.quantity)).scalar() or 0

    low_stock = db.query(Product).filter(Product.reorder_level > 0).count()

    receipts = db.query(Operation).filter(Operation.type == "receipt").count()

    deliveries = db.query(Operation).filter(Operation.type == "delivery").count()

    transfers = db.query(Operation).filter(Operation.type == "transfer").count()

    return {
        "total_stock": total_stock,
        "low_stock_products": low_stock,
        "receipts": receipts,
        "deliveries": deliveries,
        "transfers": transfers
    }