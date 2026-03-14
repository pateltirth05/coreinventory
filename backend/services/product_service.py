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


def update_product(db, product_id: int, product_data):

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise Exception("Product not found")

    product.name = product_data.name
    product.sku = product_data.sku
    product.category = product_data.category
    product.unit = product_data.unit
    product.reorder_level = product_data.reorder_level

    db.commit()
    db.refresh(product)

    return {
        "message": "Product updated",
        "product_id": product.id
    }


def filter_products_by_category(db, category: str | None = None):

    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    products = query.all()

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