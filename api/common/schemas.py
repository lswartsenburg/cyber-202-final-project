from pydantic import BaseModel


class ExceptionSchema(BaseModel):
    code: int
    name: str
    description: str
