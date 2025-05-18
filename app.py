import json
import pickle
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from typing import List
import os

# Create the FastAPI app
app = FastAPI()

# Set up templates
templates = Jinja2Templates(directory="templates")

# Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Define input data model for API
class HouseData(BaseModel):
    data: dict

# Define routes
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/predict_api")
def predict_api(house_data: HouseData):
    data = house_data.data
    print(data)
    input_array = np.array(list(data.values())).reshape(1, -1)
    print(input_array)
    new_data = scalar.transform(input_array)
    output = regmodel.predict(new_data)
    print(output[0])
    return {"prediction": float(output[0])}

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    form_data = await request.form()
    data = [float(x) for x in form_data.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "prediction_text": f"The House price prediction is {output}"}
    )

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)