def calculate_trend(df):
    return df.groupby(df['Date'].dt.year)['Temperature'].mean()
