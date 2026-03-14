from models.product import Product
# Business logic stays separate from API routes
def create_product(db, product_data):
    product = Product(**product_data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
def search_products(db, keyword: str):

    products = db.query(Product).filter(
        Product.sku.ilike(f"%{keyword}%") |
        Product.name.ilike(f"%{keyword}%")
    ).all()

    results = []

    for p in products:
        results.append({
            "id": p.id,
            "name": p.name,
            "sku": p.sku,
            "category": p.category,
            "unit": p.unit,
            "reorder_level": p.reorder_level
        })

    return results