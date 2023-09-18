from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

from router.user import router as userRouter
from router.ticket import router as ticketRouter
from router.status import router as statusRouter
from router.comment import router as commentRouter

app.include_router(userRouter, prefix="/user", tags=["user"])
app.include_router(ticketRouter, prefix="/ticket", tags=["ticket"])
app.include_router(statusRouter, prefix="/status", tags=["status"])
app.include_router(commentRouter, prefix="/comment", tags=["comment"])

#### Added by frontend team 
origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#### - we love you

# will show all available routes later
@app.get("/")
def read_root():
    return {"Hello": "World"}