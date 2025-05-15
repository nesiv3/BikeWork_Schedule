from fastapi import FastAPI
from api import schedule

app = FastAPI()
app.include_router(schedule.router, prefix="/api", tags=["schedule"])