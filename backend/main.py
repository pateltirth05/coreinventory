from fastapi import FastAPI
from routes.product_routes import router as product_router

app = FastAPI(title="Inventory Management System")

app.include_router(product_router)

@app.get("/")
def root():
    return {"message": "Inventory API running"}