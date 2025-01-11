from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

dir_static = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'static')

dir_templates = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
print(f"dir static = {dir_static}")
print(f"dir templates = {dir_templates}")

app.mount("/static", StaticFiles(directory=dir_static), name="static")


templates = Jinja2Templates(directory=dir_templates)

# @app.get("/descr/{id}", response_class=HTMLResponse)
# async def descr(request: Request, id: str):
#     filename = f"{id}.html"
#     print(f"filename={filename}")
#     return templates.TemplateResponse(
#         request=request, name=filename
#     )

@app.get("/", response_class=HTMLResponse)
async def two(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

# @app.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         request=request, name="1.html"
#     )

@app.get("/json")
async def api_json():
    print("massage: Hello World ")
    return {"message": "Hello World"}

@app.get("/json2")
async def api_json2():
    print("massage: Hello World ")
    return {"message": "Hello World"}

@app.get("/json3")
async def api_json3():
    print("massage: Hello World ")
    return {"message": "Hello World"}

