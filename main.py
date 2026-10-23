from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from models import Stable

app = FastAPI(title="EquiMatch")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(
        request: Request,
        db: Session = Depends(get_db),
        warm_wash: bool = False,
        summer_wash: bool = False,
        arena: bool = False,
        levalds: bool = False,
        vet: bool = False,
        solarium: bool = False
):
    query = db.query(Stable)

    if warm_wash:
        query = query.filter(Stable.has_warm_wash == True)
    if summer_wash:
        query = query.filter(Stable.has_summer_wash == True)
    if arena:
        query = query.filter(Stable.has_indoor_arena == True)
    if levalds:
        query = query.filter(Stable.has_levalds == True)
    if vet:
        query = query.filter(Stable.has_vet == True)
    if solarium:
        query = query.filter(Stable.has_solarium == True)

    stables = query.all()

    stables_json = [
        {"id": s.id, "name": s.name, "lat": s.lat, "lon": s.lon, "price_board": s.price_board,
         "price_training": s.price_training}
        for s in stables
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "stables": stables,
            "stables_json": stables_json,
            "filters": {
                "warm_wash": warm_wash,
                "summer_wash": summer_wash,
                "arena": arena,
                "levalds": levalds,
                "vet": vet,
                "solarium": solarium
            }
        }
    )