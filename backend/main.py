from fastapi import FastAPI

app = FastAPI()

from router import user, ticket

app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(ticket.router, prefix="/ticket", tags=["ticket"])
