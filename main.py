import argparse
from data import get_prices
from strat import add_signals, run_backtest
from metrics import (total_return, annualised_return,
                     annualised_volatility, sharpe_ratio, max_drawdown)
from plotting import plot_equity_curves, plot_signals


def print_report(name, cumulative, daily_returns):
    print(f"--- {name} ---")
    print(f"Total return:         {total_return(cumulative):.1%}")
    print(f"Annualised return:    {annualised_return(cumulative):.1%}")
    print(f"Annualised volatility:{annualised_volatility(daily_returns):.1%}")
    print(f"Sharpe ratio:         {sharpe_ratio(daily_returns):.2f}")
    print(f"Max drawdown:         {max_drawdown(cumulative):.1%}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Moving average backtester")
    parser.add_argument("--ticker", default="AAPL")
    parser.add_argument("--short", type=int, default=50)
    parser.add_argument("--long", type=int, default=200)
    parser.add_argument("--start", default="2015-01-01")
    parser.add_argument("--end", default="2025-01-01")
    args = parser.parse_args()

    prices = get_prices(args.ticker, args.start, args.end)
    df = add_signals(prices, args.short, args.long)
    df = run_backtest(df)

    print_report("Buy and hold", df["market_cumulative"], df["market_return"])
    print_report("Strategy", df["strategy_cumulative"], df["strategy_return"])

    plot_equity_curves(df, args.ticker)
    plot_signals(df, args.ticker)


if __name__ == "__main__":
    main()