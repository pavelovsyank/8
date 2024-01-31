from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

dir_static = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'static')

dir_templates = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
#print(f"dir static = {dir_static}")
#print(f"dir templates = {dir_templates}")

app.mount("/static", StaticFiles(directory=dir_static), name="static")


templates = Jinja2Templates(directory=dir_templates)


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )
@app.get("/read/{id}", response_class=HTMLResponse)
async def read_item2(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="bb.html", context={"id": id}
    )


@app.get("/produkt/{item_id}")
async def read_item(item_id):
    return {"produkt_id": item_id}

@app.get("/")
async def root():
    return {"message": "Hello World"}