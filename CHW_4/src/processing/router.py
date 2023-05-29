from pydantic.types import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_config import current_user
from src.auth.schemas import UserRead
from src.processing.schemas import Dish, Order
from src.database import get_async_session
from src.processing.models import dish, order, order_dish

router = APIRouter(
    prefix="/processing",
    tags=["Order"]
)


# Get list from "dish", quantity != 0
@router.get("/get_menu", response_model=List[Dish])
async def get_menu(session: AsyncSession = Depends(get_async_session)):
    query = select(dish).where(dish.c.quantity != 0)
    result = await session.execute(query)
    return result.all()


# Add new order to database and new items to order_dish
@router.post("/add_order")
async def add_order(new_order: Order, session: AsyncSession = Depends(get_async_session),
                    user: UserRead = Depends(current_user)):
    # If user role is not "customer" raise Exception
    if user.role_name != "customer":
        raise HTTPException(status_code=404, detail="User is not customer")

    # Get dict with info about order, status = "accepted" -- default
    order_info = {'user_id': user.id, 'status': "accepted", 'special_requests': new_order.special_requests}

    # Insert to database
    stmt = insert(order).values(order_info)
    await session.execute(stmt)
    await session.commit()

    # I'm really sorry for the code below
    dished_info = {}

    # Try to validate data (don't check types)
    for d in new_order.dishes:
        cur_d = d.split('-')
        if len(cur_d) != 2:
            raise HTTPException(status_code=404, detail=f"Incorrect index or quantity {cur_d}.")
        dished_info[cur_d[0]] = cur_d[1]

    # Get available dishes
    dishes = await session.execute(select(dish).where(dish.c.quantity != 0))
    # Get them id
    result = [d.id for d in dishes]
    # Try got id cur order))0)
    ord = await session.execute(select(order).order_by('id'))
    ind = ord.all()[0]

    for d in dished_info.keys():
        # Check id exist
        if int(d) not in result:
            raise HTTPException(status_code=404, detail=f"Dish {d} do not exist.")
        # Try got dish with cur id))0)
        cur_dish = await session.execute(select(dish).where(dish.c.id == int(d)))
        res = cur_dish.all()[0]
        # Check relevant quantity
        if int(dished_info[d]) > res.quantity:
            raise HTTPException(status_code=404, detail=f"Quantity exceeded.")

        # Get dict with info about order dish
        order_d = {'order_id': ind.id, 'dish_id': int(d), 'quantity': int(dished_info[d]), 'price_int': res.price_int,
                   'price_frac': res.price_frac}
        # Insert to database!!!!
        stmt = insert(order_dish).values(order_d)
        await session.execute(stmt)
        await session.commit()
        # You do that!! Sorry again
    return {"status": "success"}
