from fastapi import FastAPI, Depends, HTTPException, status, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
import uvicorn
import json
import re
import os
from Model.model import Model

app = FastAPI()

# Configure templates
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
model= Model()
query_engine = model.load_model()
@app.get("/")
async def index(request: Request):
    
    
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get_answer")
async def get_answer(request: Request, question: str = Form(...)):
    print(question)
    response=str(model.get_answer(question,query_engine))
    print(type(str(response)))
    # answer, relevant_documents = get_result(question)
    # response_data = jsonable_encoder(json.dumps({"answer": answer, "relevant_documents": relevant_documents}))
    # response="The provided context does not mention Raghu or anyone from the Thinkbyte team, so I cannot answer this question."
    res = Response(content=response)
    return res