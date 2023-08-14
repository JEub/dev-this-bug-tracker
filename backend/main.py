from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

from router.user import router as userRouter
from router.ticket import router as ticketRouter

app.include_router(userRouter, prefix="/user", tags=["user"])
app.include_router(ticketRouter, prefix="/ticket", tags=["ticket"])

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