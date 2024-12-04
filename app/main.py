from fastapi import FastAPI
from app.routes import user_routes, auth_routes
from app.database import engine, Base

app = FastAPI()


app.include_router(user_routes.router)
app.include_router(auth_routes.router)

@app.on_event("startup")
async def create_tables():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to Event Manager API"}
