from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Blogy AI Engine")

app.include_router(router)