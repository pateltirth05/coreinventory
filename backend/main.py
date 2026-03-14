from fastapi import FastAPI
from routes.product_routes import router as product_router
from routes.warehouse_routes import router as warehouse_router
from routes.stock_routes import router as stock_router
from routes.receipt_routes import router as receipt_router
from routes.delivery_routes import router as delivery_router
from routes.transfer_routes import router as transfer_router
from routes.adjustment_routes import router as adjustment_router
from routes.dashboard_routes import router as dashboard_router
from routes.auth_routes import router as auth_router
app = FastAPI(title="Inventory Management System")

app.include_router(product_router)
app.include_router(warehouse_router)
app.include_router(stock_router)
app.include_router(receipt_router)
app.include_router(delivery_router)
app.include_router(transfer_router)
app.include_router(adjustment_router)
app.include_router(dashboard_router)
app.include_router(auth_router)
@app.get("/")
def root():
    return {"message": "Inventory API running"}