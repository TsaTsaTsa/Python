from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey

from src.auth.models import user

metadata = MetaData()

# Model datatable with dish
dish = Table(
    "dish",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("price_int", Integer),
    Column("price_frac", Integer),
    Column("quantity", Integer),
)

# Model datatable with order
order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("status", String),
    Column("special_requests", String),
    Column("create_at", TIMESTAMP, default=datetime.utcnow),
    Column("update_at", TIMESTAMP, default=datetime.utcnow),
)

# Model datatable with order_dish
order_dish = Table(
    "order_dish",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey(order.c.id)),
    Column("dish_id", Integer, ForeignKey(dish.c.id)),
    Column("quantity", Integer),
    Column("price_int", Integer, nullable=False),
    Column("price_frac", Integer, nullable=False)
)
