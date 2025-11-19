# Fitness Prediction - Binary Classification
ML_Project

🏋️‍♂️ Problem Statement — Fitness Classification (Real-World Style Synthetic Dataset)
📌 Overview

This project focuses on solving a binary classification problem using a synthetic dataset that simulates real-world health and lifestyle data.
The goal is to predict whether a person is fit (is_fit = 1) or not fit (is_fit = 0) based on various physiological and behavioral features.

Although the dataset is synthetic, it is intentionally designed to include the same complexities and imperfections found in real-world datasets—making it ideal for learning and practicing machine learning workflows such as data cleaning, preprocessing, feature engineering, and building predictive models (including neural networks).

🧩 Problem Statement

Predicting fitness levels from health metrics is a common requirement in healthcare, wellness apps, smart devices, and fitness platforms.
However, real-world datasets often contain noise, missing values, inconsistent data types, and outliers.

The objective of this project is to build a machine learning model that can accurately classify whether an individual is fit or not based on features such as:

Age

Height & weight

Resting heart rate

Blood pressure

Sleep duration

Nutrition quality

Activity index

Smoking habits

Gender

The challenge lies not only in training the model but also in wrangling messy, inconsistent, and noisy data to create a robust input pipeline.

📊 Dataset Description

Dataset: Real-World Style Fitness Classification Dataset (Synthetic)
Samples: 2000
Task: Binary classification (is_fit = 0 or 1)
Features: 9 predictors + 1 target
Target Distribution: ~60% Not Fit, ~40% Fit
Source: Kaggle (Fitness Classification Dataset – Synthetic)

This dataset simulates realistic health and lifestyle data, containing a mix of numerical and categorical variables. It is designed with intentional imperfections to resemble real-world challenges.

🧬 Column Descriptions
Column	Description
age	Age of the individual (integer)
height_cm	Height in centimeters (integer)
weight_kg	Weight in kilograms (integer, contains outliers)
heart_rate	Resting heart rate (float)
blood_pressure	Systolic blood pressure (float)
sleep_hours	Average hours of sleep (float, contains missing values)
nutrition_quality	Nutrition score from 0–10 (float)
activity_index	Physical activity score from 1–5 (float)
smokes	Smoking status (mixed values: 0, 1, "yes", "no")
gender	Gender: "M" or "F"
is_fit	Target: 1 = fit, 0 = not fit