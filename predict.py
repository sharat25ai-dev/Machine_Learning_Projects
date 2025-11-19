import pickle
import pandas as pd

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

person = {
    "age": 69,
    "height_cm": 186,
    "weight_kg": 95,
    "heart_rate": 60.8,
    "blood_pressure": 114.8,
    "sleep_hours": 7.5,
    "nutrition_quality": 8.77,
    "activity_index": 3.19,
    "smokes": 0,
    "is_male": 0
}

X = pd.DataFrame([person])
fitness = pipeline.predict_proba(X)[0,1]
print('Prob of person being fit is =',fitness)

if(fitness>=0.5):
    print('Person is fit')
else:
    print('Person is not fit')