from fastapi import FastAPI ,WebSocket
from fastapi import Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import settings

templates = Jinja2Templates(directory="templates")

app= FastAPI()

@app.get('/')
async def home(request:Request):
    return templates.TemplateResponse("general_pages/homepage.html",{"request":request})


WebSocket_list=[]
@app.websocket('/ws')
async def websocket_endpoints(websocket : WebSocket):
    await websocket.accept()
    if websocket not in WebSocket_list:
        WebSocket_list.append(websocket)
    while True:
        data = await websocket.receive_text()
        for web in WebSocket_list:
            if web!= websocket:
                await web.send_text(f"{data}")