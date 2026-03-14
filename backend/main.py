from fastapi import FastAPI
from routes.product_routes import router as product_router
from routes.warehouse_routes import router as warehouse_router
from routes.stock_routes import router as stock_router
from routes.receipt_routes import router as receipt_router
app = FastAPI(title="Inventory Management System")

app.include_router(product_router)
app.include_router(warehouse_router)
app.include_router(stock_router)
app.include_router(receipt_router)
@app.get("/")
def root():
    return {"message": "Inventory API running"}