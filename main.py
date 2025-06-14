from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rotas import router

app = FastAPI()
app.include_router(router)

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclua o router das suas rotas
app.include_router(router)
