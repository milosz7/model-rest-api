from fastapi import FastAPI
from routes.info import router as info_router
from routes.model import router as model_router

app = FastAPI()
app.include_router(info_router)
app.include_router(model_router)
