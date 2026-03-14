from pydantic import BaseModel
# Validates incoming request data
class WarehouseCreate(BaseModel):
    name: str
    location: str | None = None