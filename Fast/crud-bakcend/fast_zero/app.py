from fastapi import FastAPI

from fast_zero.routers import activity, customers, todos

app = FastAPI()

app.include_router(todos.router)
app.include_router(customers.router)
app.include_router(activity.router)
