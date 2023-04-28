from fastapi import FastAPI, Request
import pandas as pd
import json

df_deforestation = pd.read_csv("amazon_rainforest/def_area_2004_2019.csv")
df_deforestation.rename(columns={"Ano/Estados": "Year"}, inplace=True)
df_deforestation.index = df_deforestation["Year"]

app = FastAPI();

@app.get("/blah")
async def root():
    return {"message": "Hello frodfsfm Amazon Forest"}

@app.get("/deforestation")
async def get_deforestation(year: int):
    row = 