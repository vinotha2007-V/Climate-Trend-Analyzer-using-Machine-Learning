import matplotlib.pyplot as plt

def plot_trend(trend):
    plt.plot(trend.index, trend.values)
    plt.title("Temperature Trend")
    plt.xlabel("Year")
    plt.ylabel("Temperature")
    plt.show()
