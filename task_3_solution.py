import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from copy import deepcopy
from tqdm import tqdm

from sklearn.datasets import make_regression
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
%matplotlib inline

# Задание 1
def split_data_into_two_samples(df):
    return train_test_split(df, test_size=0.3, random_state=42)

# Задание 2
def prepare_data(df):
    objects = df.select_dtypes(include=['object']).dtypes
    y = df["price_doc"]
    X = df.drop(columns=["price_doc"])
    X = X.drop(columns=objects.index)
    X = X.dropna()
    return X, y

# Задание 3
def scale(df, scaler):
    df_scaled = scaler.fit_transform(df)
    return df_scaled

# Задание 4
def prepare_data_for_model(df, scaler):
    objects = df.select_dtypes(include=['object']).dtypes
    y = df["price_doc"]
    X = df.drop(columns=["price_doc"])
    X = X.drop(columns=objects.index)
    X = X.dropna()
    df_scaled = scaler.fit_transform(X)
    return df_scaled, y

# Задание 5
def fit_first_linear_model(x_train, y_train):
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model

# Задание 6

    
# Задание 7
def evaluate_model(model, X_train, y_train):
    y_pred = model.predict(X_train[numeric_features])
    MSE = round(np.sqrt(mean_squared_error(y_train, y_pred)),2)
    MAE = round(mean_absolute_error(y_train, y_pred),2)
    R2 =  round(r2_score(y_train, y_pred),2)
    return MSE, MAE, R2


# Задание 9
# написать функцию `calculate_squared_stats_by_material`, которая принимает на вход датафрейм `X` и возвращает максимальную 
# и минимальную площадь квартир в зависимости от материала изготовления дома. Каждое значение площади округлить до 2-го знака.
def calculate_squared_stats_by_material(x):
    pivot_table = pd.pivot_table(x, index=['material'], values='full_sq', aggfunc={'full_sq': [np.max, np.min]})
    return round(pivot_table, 2)

# Задание 10
# написать функцию `calculate_crosstab`, которая принимает на вход датафрейм X и возвращает максимальную и минимальную стоимость 
# квартир в зависимости от района города и цели покупки. 
# Ответ - сводная таблица, где индекс - район города (признак - `sub_area`),
# столбцы - цель покупки (признак - `product_type`). Каждое значение цены округлить до 2-го знака, пропуски заполнить нулем.
def calculate_crosstab(x):
    cross_table = pd.crosstab(index=x['sub_area'], columns=x['product_type'], values=x['price_doc'], aggfunc=np.mean).fillna(0)
    return round(cross_table, 2)
