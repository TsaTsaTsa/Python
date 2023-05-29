from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

from src.database import Base

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, nullable=False),
    Column("name", String, unique=True),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(length=100), nullable=False, unique=True),
    Column("username", String(length=50), nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("update_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_name", String, ForeignKey(role.c.name)),
    Column("hashed_password", String(length=255), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

session = Table(
    "session",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("session_token", String),
    Column("expires_at", TIMESTAMP, default=datetime.utcnow),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(length=100), nullable=False, unique=True)
    username = Column(String(length=50), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    update_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_name = Column(String, ForeignKey(role.c.name))
    hashed_password = Column(String(length=255), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
