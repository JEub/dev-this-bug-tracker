from fastapi import FastAPI

app = FastAPI()

from router.user import router as userRouter
from router.ticket import router as ticketRouter
from router.status import router as statusRouter
from router.comment import router as commentRouter

app.include_router(userRouter, prefix="/user", tags=["user"])
app.include_router(ticketRouter, prefix="/ticket", tags=["ticket"])
app.include_router(statusRouter, prefix="/status", tags=["status"])
app.include_router(commentRouter, prefix="/comment", tags=["comment"])

# will show all available routes later
@app.get("/")
def read_root():
    return {"Hello": "World"}