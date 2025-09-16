from fastapi import FastAPI
from app.api import routes

app = FastAPI()

# include routers
app.include_router(routes.router)
