from fastapi import FastAPI

from src.auth.router import router_reg, router_auth, router_info
from src.processing.router import router as router_operation


app = FastAPI(
    title="Restaurant App"
)

# Router for login/logout
app.include_router(
    router_auth,
    prefix="/auth",
    tags=["Auth"],
)

# Router for sing in
app.include_router(
    router_reg,
    prefix="/auth",
    tags=["Auth"]
)

# Router for get info about user
app.include_router(router_info)

# Router for processing
app.include_router(router_operation)
