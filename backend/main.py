from fastapi import FastAPI

app = FastAPI()

from router.user import router as userRouter
from router.ticket import router as ticketRouter

app.include_router(userRouter, prefix="/user", tags=["user"])
app.include_router(ticketRouter, prefix="/ticket", tags=["ticket"])

# will show all available routes later
@app.get("/")
def read_root():
    return {"Hello": "World"}