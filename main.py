import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.main.classes.connector.Connector import Connector
from src.main.run import RunEngine
from fastapi.middleware.cors import CORSMiddleware
run = RunEngine()

app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.post("/api/start")
# def start():
#     ads = run.plugin.get_data()
#     run.connector = Connector(ads)
#     run.run_engine()
#     return {"response": {"ads": ads, "ratings": run.plugin.interests, "seed": run.seed}}


# @app.post("/api/process")
# def process(input: Input):
#     input = json.loads(input.message)
#     clean_input(input)
#     new_data = run.plugin.change_data(input)
#     run.connector = Connector(new_data)
#     run.run_engine()
#     return {"response": {"ads": new_data, "ratings": run.plugin.interests, "seed": run.seed}}


@app.post("/api/data")
def get_sample_data():
    data = {
        "data": [
            {"id": 1, "name": "Sample Item 1", "value": 100},
            {"id": 2, "name": "Sample Item 2", "value": 200},
            {"id": 3, "name": "Sample Item 3", "value": 300}
        ],
        "total": 3,
        "timestamp": "2024-01-01T00:00:00Z"
    }

    return data

    # return {
    #     "statusCode": 200,
    #     "headers": {
    #         "Access-Control-Allow-Origin": "*",
    #         "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
    #         "Access-Control-Allow-Headers": "Content-Type",
    #     },
    #     "body": json.dumps(data)
    # }



@app.get("/")
def read_root():
    ads = run.plugin.get_data()
    run.connector = Connector(ads)
    run.run_engine()
    return {"response": {"ads": ads, "ratings": run.plugin.interests, "seed": run.seed}}

