from fastapi import FastAPI


app = FastAPI()


@app.get("/ping/", summary="Get test message")
def ping():

    return {"message": "pong"}