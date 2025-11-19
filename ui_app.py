from typing import Literal
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app = FastAPI()

# Pydantic model
class UserData(BaseModel):
    age: Annotated[float, Field(ge=1, le=100)]
    height_cm: Annotated[float, Field(ge=100, le=250)]
    weight_kg: Annotated[float, Field(ge=30, le=250)]
    heart_rate: Annotated[float, Field(ge=45, le=150)]
    blood_pressure: Annotated[float, Field(ge=75, le=250)]
    sleep_hours: Annotated[float | None, Field(ge=1, le=24)] = None
    nutrition_quality: Annotated[float, Field(ge=0, le=10)]
    activity_index: Annotated[float, Field(ge=1, le=5)]
    smokes: Literal[0, 1]
    is_male: Literal[0, 1]

# Home page with enhanced UI
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head>
        <title>User Data Prediction</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h2 { color: #333; }
            form { display: grid; grid-gap: 15px; max-width: 500px; }
            label { font-weight: bold; }
            input[type="submit"] { padding: 10px; font-size: 16px; cursor: pointer; }
            .slider-value { font-weight: normal; margin-left: 10px; }
        </style>
    </head>
    <body>
        <h2>Enter User Data for Prediction</h2>
        <form action="/predict" method="post">
            <label>Age: <span id="age_val">50</span></label>
            <input type="range" name="age" min="1" max="100" value="50" oninput="age_val.innerText=this.value">
            
            <label>Height (cm): <span id="height_val">170</span></label>
            <input type="range" name="height_cm" min="100" max="250" value="170" step="0.1" oninput="height_val.innerText=this.value">
            
            <label>Weight (kg): <span id="weight_val">70</span></label>
            <input type="range" name="weight_kg" min="30" max="250" value="70" step="0.1" oninput="weight_val.innerText=this.value">
            
            <label>Heart Rate: <span id="hr_val">70</span></label>
            <input type="range" name="heart_rate" min="45" max="150" value="70" step="0.1" oninput="hr_val.innerText=this.value">
            
            <label>Blood Pressure: <span id="bp_val">120</span></label>
            <input type="range" name="blood_pressure" min="75" max="250" value="120" step="0.1" oninput="bp_val.innerText=this.value">
            
            <label>Sleep Hours: <span id="sleep_val">7</span></label>
            <input type="range" name="sleep_hours" min="1" max="24" value="7" step="0.1" oninput="sleep_val.innerText=this.value">
            
            <label>Nutrition Quality (0-10): <span id="nutr_val">5</span></label>
            <input type="range" name="nutrition_quality" min="0" max="10" value="5" step="0.01" oninput="nutr_val.innerText=this.value">
            
            <label>Activity Index (1-5): <span id="act_val">3</span></label>
            <input type="range" name="activity_index" min="1" max="5" value="3" step="0.01" oninput="act_val.innerText=this.value">
            
            <label>Smokes:</label>
            <select name="smokes">
                <option value="0">No</option>
                <option value="1">Yes</option>
            </select>
            
            <label>Is Male:</label>
            <select name="is_male">
                <option value="0">No</option>
                <option value="1">Yes</option>
            </select>
            
            <input type="submit" value="Predict">
        </form>
    </body>
    </html>
    """

# POST endpoint
@app.post("/predict")
async def predict(
    age: float = Form(...),
    height_cm: float = Form(...),
    weight_kg: float = Form(...),
    heart_rate: float = Form(...),
    blood_pressure: float = Form(...),
    sleep_hours: float | None = Form(None),
    nutrition_quality: float = Form(...),
    activity_index: float = Form(...),
    smokes: int = Form(...),
    is_male: int = Form(...)
):
    # Validate and create Pydantic object
    user_data = UserData(
        age=age,
        height_cm=height_cm,
        weight_kg=weight_kg,
        heart_rate=heart_rate,
        blood_pressure=blood_pressure,
        sleep_hours=sleep_hours,
        nutrition_quality=nutrition_quality,
        activity_index=activity_index,
        smokes=smokes,
        is_male=is_male
    )

    # Example prediction logic
    prediction = user_data.age * 0.1 + user_data.activity_index * 2  # replace with your model

    return {"prediction": prediction, "input_data": user_data.dict()}
