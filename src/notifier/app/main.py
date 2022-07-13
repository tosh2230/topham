from typing import Optional

from fastapi import FastAPI

notifier = FastAPI()


@notifier.get("/")
def introduce_myself():
    return {"message": "I am a notifier."}


@notifier.get("/notices/{notification_id}")
def inform(notification_id: int, q: Optional[str] = None):
    return {
        "notification_id": notification_id,
        "q": q,
    }
