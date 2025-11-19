# Fitness Prediction - Binary Classification
📘 Dataset Description

This synthetic dataset simulates a real-world fitness classification problem where the objective is to predict fitness status using lifestyle and health features. The data contains noise, inconsistencies, outliers, and missing values to reflect actual industry datasets.

It is particularly useful for learners practicing preprocessing, feature engineering, and classification model building.

🧬 Column Descriptions
Column Name	Description
age	Age of the individual in years
height_cm	Height in centimeters
weight_kg	Weight in kilograms (contains outliers)
heart_rate	Resting heart rate (bpm)
blood_pressure	Systolic blood pressure (mmHg)
sleep_hours	Average sleep duration (contains missing values)
nutrition_quality	Nutrition quality score (0–10)
activity_index	Physical activity score (1–5)
smokes	Smoking status (mixed numeric + string categories)
gender	‘M’ or ‘F’
is_fit	Target variable (1 = fit, 0 = not fit)
📊 Dataset Statistics

Total samples: 2000

Features: 10 (9 inputs + 1 target)

Class balance: ~60% Not Fit, ~40% Fit

Missing values: ~8% in sleep_hours

Outliers: Present in weight_kg

Data types: Mixed (int, float, string)

Noise: Added for realism

🧠 What I Did in This Project

To prepare the dataset and build the final model, I performed the following steps:

✅ 1. Handle Mixed Data Types

Converted mixed smokes values (0, 1, "yes", "no") into consistent binary encoding (0 = non-smoker, 1 = smoker).

✅ 2. Encode Categorical Variables

Converted gender into numerical form using a custom encoding:

is_male = 1

is_male = 0

✅ 3. Handle Missing Values

Imputed missing values in sleep_hours using the median, which is robust to outliers.

✅ 4. Scaling

Standardized all numerical features using StandardScaler inside a pipeline (important for logistic regression and distance-based models).

✅ 5. Model Training and Evaluation

Trained multiple models using tuned hyperparameters and evaluated them using Validation ROC-AUC:

Model	Validation ROC-AUC	Rank
Logistic Regression	0.8566	🥇 (1)
Random Forest	0.8417	🥈 (2)
XGBoost	0.8400	🥉 (3)
Decision Tree	0.7999	4
✅ 6. Final Model

Selected Logistic Regression as the final model

Trained using tuned hyperparameters

Good performance + explainability + stability

📄 License

This dataset is released under CC0 Public Domain — free for use in education, research, and development.

🙌 Acknowledgments

This is a synthetic dataset created for safe educational use.
It does not include any real personal information and is intended for learning data science, machine learning, and preprocessing techniques.


