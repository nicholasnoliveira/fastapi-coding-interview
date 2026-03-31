from fastapi import FastAPI

from app.routes import users, courses

app = FastAPI(title="BEON High School API")

app.include_router(users.router)
app.include_router(courses.router)
