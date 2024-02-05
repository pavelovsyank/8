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



@app.get("/chery/{id}", response_class=HTMLResponse)
async def chery(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="cucumber.html", context={"id": id}
    )
@app.get("/cucumber/{id}", response_class=HTMLResponse)
async def cucumber(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="cucumber.html", context={"id": id}
    )
@app.get("/apple/{id}", response_class=HTMLResponse)
async def apple(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="apple.html", context={"id": id}
    )
@app.get("/melon/{id}", response_class=HTMLResponse)
async def melon(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="melon.html", context={"id": id}
    )
@app.get("/watermelon/{id}", response_class=HTMLResponse)
async def watermelon(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="watermelon.html", context={"id": id}
    )
@app.get("/tomato/{id}", response_class=HTMLResponse)
async def tomato(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="tomato.html", context={"id": id}
    )
@app.get("/grape/{id}", response_class=HTMLResponse)
async def grape(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="grape.html", context={"id": id}
    )
@app.get("/blackberries/{id}", response_class=HTMLResponse)
async def blackberries(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="blackberries.html", context={"id": id}
    )
@app.get("/pear/{id}", response_class=HTMLResponse)
async def pear(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="pear.html", context={"id": id}
    )
@app.get("/potato/{id}", response_class=HTMLResponse)
async def potato(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="potato.html", context={"id": id}
    )
@app.get("/apricot/{id}", response_class=HTMLResponse)
async def apricot(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="apricot.html", context={"id": id}
    )
@app.get("/pineapple/{id}", response_class=HTMLResponse)
async def pineapple(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="pineapple.html", context={"id": id}
    )
@app.get("/avocado/{id}", response_class=HTMLResponse)
async def avocado(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="avocado.html", context={"id": id}
    )
@app.get("/banana/{id}", response_class=HTMLResponse)
async def banana(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="banana.html", context={"id": id}
    )
@app.get("/kiwi/{id}", response_class=HTMLResponse)
async def kiwi(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="kiwi.html", context={"id": id}
    )
@app.get("/lime/{id}", response_class=HTMLResponse)
async def lime(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="lime.html", context={"id": id}
    )
@app.get("/lemon/{id}", response_class=HTMLResponse)
async def lemon(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="lemon.html", context={"id": id}
    )
@app.get("/mango/{id}", response_class=HTMLResponse)
async def mango(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="mango.html", context={"id": id}
    )
@app.get("/orange/{id}", response_class=HTMLResponse)
async def orange(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="orange.html", context={"id": id}
    )
@app.get("/pomelo/{id}", response_class=HTMLResponse)
async def pomelo(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="pomelo.html", context={"id": id}
    )
@app.get("/carrot/{id}", response_class=HTMLResponse)
async def carrot(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="carrot.html", context={"id": id}
    )
@app.get("/pepper/{id}", response_class=HTMLResponse)
async def pepper(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="pepper.html", context={"id": id}
    )
@app.get("/coconut/{id}", response_class=HTMLResponse)
async def coconut(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="coconut.html", context={"id": id}
    )
@app.get("/broccoli/{id}", response_class=HTMLResponse)
async def broccoli(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="broccoli.html", context={"id": id}
    )
@app.get("/corn/{id}", response_class=HTMLResponse)
async def corn(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="corn.html", context={"id": id}
    )




@app.get("/produkt/{item_id}")
async def read_item(item_id):
    return {"produkt_id": item_id}

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="root.html"
    )