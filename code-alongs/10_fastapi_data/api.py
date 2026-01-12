from fastapi import FastAPI, Query
from data_processing import DataExplorer

app = FastAPI()


@app.get("/sales")
async def read_sales(limit: int = Query(10, gt=0, lt=120_000)):
    data_explorer = DataExplorer(limit=limit)
    return data_explorer.json_response()


@app.get("/summary")
async def read_summary_data():
    data_explorer = DataExplorer()
    # return summary = data_explorer.summary().json_response()
    return {"summary": "good summary of data"}
