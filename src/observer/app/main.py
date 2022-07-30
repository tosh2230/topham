from datetime import datetime as dt
import yaml
from typing import Union

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Schedule(BaseModel):
    key: str
    description: Union[str, None] = None
    table_pattern: str
    event_pattern: str
    notification_key: str
    job_delay_threshold: int = 0
    job_first_invoke_at: dt = None
    job_interval: int = 0
    job_timeout: int = 0


app = FastAPI()


@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"message": str(exc)})


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=400, content={"message": str(exc)})


@app.get("/")
def whoami():
    return {"message": "I am a observer."}


@app.get("/schedules/{schedule_key}")
async def observe(schedule_key: str):
    return get_schedule(key=schedule_key)


def get_schedule(key: str) -> Schedule:
    with open("/app/config/schedules.yaml") as f:
        schedules = yaml.safe_load(f)
    schedule_dict = schedules.get(key)

    if not schedule_dict:
        raise HTTPException(status_code=404, detail="Schedule not found")

    return Schedule(
        key=key,
        description=schedule_dict.get("description"),
        table_pattern=schedule_dict.get("table_pattern"),
        event_pattern=schedule_dict.get("event_pattern"),
        notification_key=schedule_dict.get("notification_key"),
        job_delay_threshold=schedule_dict.get("job_delay_threshold", 0),
        job_first_invoke_at=dt.strptime(
            schedule_dict.get("job_first_invoke_at"), "%Y-%m-%d %H:%M:%S%z"
        ),
        job_interval=schedule_dict.get("job_interval", 0),
        job_timeout=schedule_dict.get("job_timeout", 0),
    )
