from pydantic import BaseModel

class Account(BaseModel):
    username: str
    password: str

class Verification(BaseModel):
    username: str
    password: str