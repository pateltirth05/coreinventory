from fastapi import FastAPI
from routes.product_routes import router as product_router
from routes.warehouse_routes import router as warehouse_router

app = FastAPI(title="Inventory Management System")

app.include_router(product_router)
app.include_router(warehouse_router)

@app.get("/")
def root():
    return {"message": "Inventory API running"}