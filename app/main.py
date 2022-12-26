from api.api_v1.api import router as api_router
from mangum import Mangum
from fastapi import FastAPI

# sys.path.insert(0, glob.glob("./env")[0])

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(api_router, prefix="/api/v1")

handler = Mangum(app)
