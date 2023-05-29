from pydantic import BaseModel


class Dish(BaseModel):
    id: int
    name: str
    description: str
    price_int: int
    price_frac: int
    quantity: int

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: int
    user_id: int
    special_requests: str
    status: str
    dishes: list

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "dishes": "{dish_id1}-{quantity}, {dish_id2}-{quantity}..."
            }
        }
