from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.database import create_tables
from api.public import api as public_api

def create_app():
    app = FastAPI(
        title="Control de Ingreso",
        version="0.1"
    )

    origins = [
        # "http://localhost:5173/",
        # "http://127.0.0.1:5173/",
        # "http://localhost:5173/admin",
        # "http://127.0.0.1:5173/admin"
        "https://control-ingreso.netlify.app/",
        "https://control-ingreso.netlify.app/admin",
        "https://control-ingreso.netlify.app/agregar"

    ]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    @app.on_event("startup")
    def on_starup():
        create_tables()


    app.include_router(public_api)

    return app 