from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(df):
    df['Year'] = df['Date'].dt.year
    X = df[['Year']]
    y = df['Temperature']

    model = LinearRegression()
    model.fit(X, y)
    return model
