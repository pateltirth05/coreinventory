from models.stock import Stock

def get_stock(db):
    return db.query(Stock).all()