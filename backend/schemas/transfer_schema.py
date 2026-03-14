from pydantic import BaseModel

class TransferItem(BaseModel):
    product_id: int
    quantity: int

class TransferCreate(BaseModel):
    source_warehouse: int
    destination_warehouse: int
    items: list[TransferItem]