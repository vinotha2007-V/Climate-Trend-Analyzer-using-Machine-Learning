def preprocess(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.fillna(method='ffill')
    return df
