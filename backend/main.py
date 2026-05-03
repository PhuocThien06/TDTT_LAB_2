from fastapi import FastAPI
from notes import router as notes_router
from auth import router as auth_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(notes_router)

app.include_router(auth_router)