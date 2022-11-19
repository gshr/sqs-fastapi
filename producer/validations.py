from pydantic import BaseModel


class Message(BaseModel):
    id: int
    table_name: str
