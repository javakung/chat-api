from fastapi import FastAPI, Header,Form, Body


app = FastAPI(
    title="Chat API",
    description="Chat Backend API",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/conversation",tags=["Conversation Unit"])
def get_conversation():
    return {"Hello": "World"}

@app.post("/conversation",tags=["Conversation Unit"])
def update_conversation():
    return {"Hello": "World"}   

@app.delete("/conversation",tags=["Conversation Unit"])
def delete_conversation(cid:str=""):
    return {"status": True}    

@app.get("/service",tags=["Service"])
def get_service():
    return {"Hello": "World"}

@app.post("/service",tags=["Service"])
def update_service():
    return {"Hello": "World"}   

@app.delete("/service",tags=["Service"])
def delete_service(sid:str=""):
    return {"status": True}    


@app.get("/chat",tags=["Chat"])
def chat(session_id:str="",incoming_message:str=""):
    return {"Hello": "World"}