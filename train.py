#!/usr/bin/env python
# coding: utf-8

# # Mid Term Project - Fitness Prediction

import pickle
import sklearn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score


print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')


def load_data():
    path = 'dataset/fitness_dataset.csv'
    df = pd.read_csv(path)

    df['smokes'] = df['smokes'].map( 
        {
        'yes': 1,
        'no': 0,
        '1': 1,
        '0': 0
        }
    )

    df['gender'] = df['gender'].map( 
        {
        'M': 1,
        'F': 0,
        }
    )

    df = df.rename(columns={'gender': 'is_male'})
    return df


def train_model(df):

    numeric_features = ['age', 'height_cm', 'weight_kg', 'heart_rate', 'blood_pressure',
        'sleep_hours', 'nutrition_quality', 'activity_index']

    categorical_features = ['smokes','is_male']

    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)    
    df_full_train = df_full_train.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    y_full_train = df_full_train.is_fit.values
    y_test = df_test.is_fit.values

    del df_full_train['is_fit']
    del df_test['is_fit']

    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = 'passthrough'

    preprocess = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )

    pipe = Pipeline(steps=[
        ('preprocess', preprocess),
        ('model', LogisticRegression(max_iter=1000))
    ])

    X_train = df_full_train
    y_train = y_full_train

    pipe.set_params(
        model__C=100,
        model__penalty='l2',
        model__solver='liblinear',
        model__max_iter=1000
    )

    pipe.fit(X_train, y_train)

    return pipe


def save_model(pipeline, output_file):
    with open(output_file, 'wb') as f_out:
        pickle.dump(pipeline, f_out)


df = load_data()
pipeline = train_model(df)
save_model(pipeline, 'model.bin')
print('Model saved to model.bin')