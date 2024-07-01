from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_bd

criar_bd()

app = FastAPI()

# CORS
origins = ['http://127.0.0.1:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
