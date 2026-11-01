from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}


