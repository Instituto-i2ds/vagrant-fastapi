from fastapi import FastAPI
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

agenda = [{'Name': 'Luis', 'Phone': 5555555555}]


app = FastAPI()

@app.get("/")
def hello():
    return {"Message": "Hello World from FastAPI"}

@app.get("/agenda")
def read_agenda():
    return {"agenda": agenda}

class Contact(BaseModel):
    name: str
    phone: int

@app.post("/contact")
async def create_contact(contact: Contact):
    contact_dict = contact.dict()
    agenda.append(contact_dict)
    return contact_dict
