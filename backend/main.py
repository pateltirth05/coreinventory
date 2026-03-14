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
from routes.movement_routes import router as movement_router
from routes.alert_routes import router as alert_router
from routes.operation_routes import router as operation_router
from routes.password_routes import router as password_router
from routes.profile_routes import router as profile_router


from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
app = FastAPI(title="Inventory Management System")

app.include_router(password_router)
app.include_router(operation_router)
app.include_router(product_router)
app.include_router(warehouse_router)
app.include_router(stock_router)
app.include_router(receipt_router)
app.include_router(delivery_router)
app.include_router(transfer_router)
app.include_router(adjustment_router)
app.include_router(dashboard_router)
app.include_router(auth_router)
app.include_router(movement_router)
app.include_router(alert_router)
app.include_router(profile_router)
@app.get("/")
def root():
    return {"message": "Inventory API running"}
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
@app.get("/dashboard")
def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
@app.get("/signup")
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.get("/forgot-password")
def forgot_password_page(request: Request):
    return templates.TemplateResponse("forgot_password.html", {"request": request})