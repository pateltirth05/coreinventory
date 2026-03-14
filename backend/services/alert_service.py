from sqlalchemy.orm import Session
from models.stock import Stock
from models.product import Product


def get_low_stock_products(db: Session):

    results = db.query(
        Product.id,
        Product.name,
        Product.sku,
        Product.reorder_level,
        Stock.quantity
    ).join(
        Stock, Product.id == Stock.product_id
    ).filter(
        Stock.quantity < Product.reorder_level
    ).all()

    alerts = []

    for r in results:
        alerts.append({
            "product_id": r.id,
            "product_name": r.name,
            "sku": r.sku,
            "current_stock": r.quantity,
            "reorder_level": r.reorder_level
        })

    return alerts