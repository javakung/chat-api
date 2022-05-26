from fastapi import FastAPI, Header,Form, Body
from pydantic import BaseModel


class ConversationUnit(BaseModel):
    text: str
    intent: str
    entities: list
    confidence: float
    response: str
    context: dict


class Service(BaseModel):
    name: str
    description: str
    version: str
    url: str
    status: str

class incoming_message(BaseModel):
    session_id: str
    text: str
    context: dict

class outgoing_message(BaseModel):
    text: str
    context: dict



app = FastAPI(
    title="Chat API",
    description="Chat Backend API",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/conversation",tags=["Conversation Unit"])
def create_conversation(conversation_unit: ConversationUnit):
    res = {
        "status": "success",
    }
    return res   

@app.get("/conversation",tags=["Conversation Unit"])
def get_conversation(cid: str):
    return {"Hello": "World"}

@app.put("/conversation",tags=["Conversation Unit"])
def update_conversation(conversation_unit: ConversationUnit):
    res = {
        "status": "success",
    }
    return res 

@app.delete("/conversation",tags=["Conversation Unit"])
def delete_conversation(cid:str=""):
    res = {
        "status": "success",
    }
    return res   


@app.post("/service",tags=["Service"])
def create_service(service:Service):

    res = {
        "status": "success",
    }
    return res 

@app.get("/service",tags=["Service"])
def get_service():
    return {"Hello": "World"}

@app.put("/service",tags=["Service"])
def update_service(service:Service):
    
    res = {
        "status": "success",
    }
    return res 

@app.delete("/service",tags=["Service"])
def delete_service(sid:str=""):

    res = {
        "status": "success",
    }
    return res  


@app.get("/chat",tags=["Chat"],response_model=outgoing_message)
def chat(inc_msg: incoming_message):
    return {"Hello": "World"}