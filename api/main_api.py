import os
from fastapi import FastAPI, Depends, Request, HTTPException
from db_engine.database import SessionLocal, engine
from sqlalchemy.orm import Session
from db_engine import models
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

#  IMPORTING SCHEMAS
# from schemas.dose_schemas import Dose
# from schemas.establishments_schemas import Establishments
# from schemas.record_chemas import Record

#  IMPORTING ROUTERS
from routers.store import store_router
from routers.category import category_router
from routers.products import products_router
from routers.brands import brands_router


#  CREATE DB MODELS
models.Base.metadata.create_all(bind=engine)


#  IMPORTING METADATA
# from api_metadata import api_metadata

app = FastAPI(
    title="Price tracker api.",
    # description="A small api to explore COVID data of Paraguay..",
    version="0.0.1",
    #  openapi_tags=api_metadata
)

#  INCLUDING ROUTERS
app.include_router(store_router.store_router)
app.include_router(category_router.category_router)
app.include_router(products_router.products_router)
app.include_router(brands_router.brands_rounter)


#  MIDLEWARE SETUP
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def api_home(request: Request):
    return "HOLA MUNDO!"
