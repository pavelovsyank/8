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
@app.get("bob/{id}", response_class=HTMLResponse)
async def bob(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="bob.html", context={"id": id}
    )
@app.get("/airline/{id}", response_class=HTMLResponse)
async def airline(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="airline.html", context={"id": id}
    )
@app.get("/auto/{id}", response_class=HTMLResponse)
async def auto(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="auto.html", context={"id": id}
    )
@app.get("/aggressive/{id}", response_class=HTMLResponse)
async def aggressive(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="aggressive.html", context={"id": id}
    )
@app.get("/address/{id}", response_class=HTMLResponse)
async def address(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="address.html", context={"id": id}
    )
@app.get("/academy/{id}", response_class=HTMLResponse)
async def academy(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="academy.html", context={"id": id}
    )
@app.get("/active/{id}", response_class=HTMLResponse)
async def active(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="active.html", context={"id": id}
    )
@app.get("/algorithm/{id}", response_class=HTMLResponse)
async def algorithm(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="algorithm.html", context={"id": id}
    )
@app.get("/alcohol/{id}", response_class=HTMLResponse)
async def alcohol(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="alcohol.html", context={"id": id}
    )
@app.get("/diamond/{id}", response_class=HTMLResponse)
async def diamond(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="diamond.html", context={"id": id}
    )
@app.get("/alternative/{id}", response_class=HTMLResponse)
async def alternative(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="alternative.html", context={"id": id}
    )
@app.get("/alpha/{id}", response_class=HTMLResponse)
async def alpha(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="alpha.html", context={"id": id}
    )
@app.get("/arena/{id}", response_class=HTMLResponse)
async def arena(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="arena.html", context={"id": id}
    )
@app.get("/arrest/{id}", response_class=HTMLResponse)
async def arrest(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="arrest.html", context={"id": id}
    )
@app.get("/atomic/{id}", response_class=HTMLResponse)
async def atomic(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="atomic.html", context={"id": id}
    )
@app.get("/atoms/{id}", response_class=HTMLResponse)
async def atoms(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="atoms.html", context={"id": id}
    )
@app.get("/audio/{id}", response_class=HTMLResponse)
async def audio(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="audio.html", context={"id": id}
    )
@app.get("/auditors/{id}", response_class=HTMLResponse)
async def auditors(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="auditors.html", context={"id": id}
    )
@app.get("/airport/{id}", response_class=HTMLResponse)
async def airport(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="airport.html", context={"id": id}
    )
@app.get("/gunman/{id}", response_class=HTMLResponse)
async def gunman(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="gunman.html", context={"id": id}
    )
@app.get("/drum/{id}", response_class=HTMLResponse)
async def drum(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="drum.html", context={"id": id}
    )
@app.get("/bass/{id}", response_class=HTMLResponse)
async def bass(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="bass.html", context={"id": id}
    )
@app.get("/battery/{id}", response_class=HTMLResponse)
async def battery(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="battery.html", context={"id": id}
    )
@app.get("/homeless/{id}", response_class=HTMLResponse)
async def homeless(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="homeless.html", context={"id": id}
    )
@app.get("/secure/{id}", response_class=HTMLResponse)
async def secure(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="secure.html", context={"id": id}
    )
@app.get("/white/{id}", response_class=HTMLResponse)
async def white(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="white.html", context={"id": id}
    )
@app.get("/beta/{id}", response_class=HTMLResponse)
async def beta(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="beta.html", context={"id": id}
    )
@app.get("/ticket/{id}", response_class=HTMLResponse)
async def ticket(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="ticket.html", context={"id": id}
    )
@app.get("/blank/{id}", response_class=HTMLResponse)
async def blank(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="blank.html", context={"id": id}
    )
@app.get("/block/{id}", response_class=HTMLResponse)
async def block(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="block.html", context={"id": id}
    )




@app.get("/produkt/{item_id}")
async def read_item(item_id):
    return {"produkt_id": item_id}

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="root.html"
    )