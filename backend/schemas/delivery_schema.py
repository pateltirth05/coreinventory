from pydantic import BaseModel

# define the strcuture of delivery requests
class DeliveryItem(BaseModel):
    product_id: int
    quantity: int


class DeliveryCreate(BaseModel):
    source_warehouse: int
    items: list[DeliveryItem]