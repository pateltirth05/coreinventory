from pydantic import BaseModel
# this will do Validates request data before reaching database
class ProductCreate(BaseModel):
    name: str
    sku: str
    category: str | None = None
    unit: str | None = None
    reorder_level: int = 0