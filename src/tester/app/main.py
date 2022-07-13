from typing import Optional

from fastapi import FastAPI

tester = FastAPI()


@tester.get("/")
def introduce_myself():
    return {"message": "I am a tester."}


@tester.get("/tests/{test_id}")
def verity(test_id: int, q: Optional[str] = None):
    return {
        "test_id": test_id,
        "q": q,
    }
