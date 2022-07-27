import os
import pyyaml
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def whoami():
    return {"message": "I am a observer."}


@app.get("/schedules/{schedule_id}")
def observe(schedule_id: int, q: Optional[str] = None):
    return {
        "schedule_id": schedule_id,
        "q": q,
    }

def get_schedule(schedule_id: int):

