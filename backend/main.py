# uvicorn main:app
# uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    print("Test route!")
    return {"message": "Hello World!"}

