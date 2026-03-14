from pydantic import BaseModel

class ReceiptItem(BaseModel):
    product_id: int
    quantity: int


class ReceiptCreate(BaseModel):
    supplier_name: str
    destination_warehouse: int
    items: list[ReceiptItem]

    # defines how the API receives receipt data 