import numpy as np

TRADING_DAYS = 252  

def total_return(cumulative):
    """Total % gain over the whole period."""
    return cumulative.dropna().iloc[-1] - 1


def annualised_return(cumulative):
    """Average yearly growth rate (compounded)."""
    cumulative = cumulative.dropna()
    years = len(cumulative) / TRADING_DAYS
    return cumulative.iloc[-1] ** (1 / years) - 1


def annualised_volatility(daily_returns):
    """How much returns bounce around, scaled to a year."""
    return daily_returns.dropna().std() * np.sqrt(TRADING_DAYS)


def sharpe_ratio(daily_returns, risk_free_rate=0.0):
    """Return earned per unit of risk. Higher is better."""
    returns = daily_returns.dropna()
    excess = returns - risk_free_rate / TRADING_DAYS
    if excess.std() == 0:
        return 0.0
    return (excess.mean() / excess.std()) * np.sqrt(TRADING_DAYS)


def max_drawdown(cumulative):
    """Worst peak-to-trough fall, as a negative %."""
    cumulative = cumulative.dropna()
    running_peak = cumulative.cummax()
    drawdown = (cumulative - running_peak) / running_peak
    return drawdown.min()