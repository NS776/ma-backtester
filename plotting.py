import matplotlib.pyplot as plt


def plot_equity_curves(df, ticker):
    """Compare strategy vs buy-and-hold growth."""
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["market_cumulative"], label="Buy and hold")
    plt.plot(df.index, df["strategy_cumulative"], label="MA crossover strategy")
    plt.title(f"{ticker}: Strategy vs Buy and Hold")
    plt.xlabel("Date")
    plt.ylabel("Growth of £1")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{ticker}_equity_curve.png", dpi=150)
    plt.show()


def plot_signals(df, ticker):
    """Show price, moving averages, and where we bought/sold."""
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Price", alpha=0.6)
    plt.plot(df.index, df["short_ma"], label="Short MA")
    plt.plot(df.index, df["long_ma"], label="Long MA")

    # When it goes from 0 to 1 its a buy and 1 to 0 its a sell
    change = df["position"].diff()
    buys = df[change == 1]
    sells = df[change == -1]

    plt.scatter(buys.index, buys["Close"], marker="^", color="green",
                s=100, label="Buy", zorder=5)
    plt.scatter(sells.index, sells["Close"], marker="v", color="red",
                s=100, label="Sell", zorder=5)

    plt.title(f"{ticker}: Signals")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{ticker}_signals.png", dpi=150)
    plt.show()