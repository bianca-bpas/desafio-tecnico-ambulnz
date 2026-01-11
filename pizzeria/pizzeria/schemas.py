from pydantic import BaseModel

class HealthCkeck(BaseModel):
    status: str = "OK"
