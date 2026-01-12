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
    return data_explorer.summary().json_response()


@app.get("/kpis")
async def read_kpis_by_country(country: str):
    data_explorer = DataExplorer()
    return data_explorer.kpis(country=country)
