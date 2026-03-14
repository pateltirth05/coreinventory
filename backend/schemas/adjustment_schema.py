from pydantic import BaseModel

class AdjustmentItem(BaseModel):
    product_id: int
    warehouse_id: int
    counted_quantity: int


class AdjustmentCreate(BaseModel):
    items: list[AdjustmentItem]