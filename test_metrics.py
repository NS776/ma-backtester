import pandas as pd
from metrics import total_return, max_drawdown


def test_total_return():
    cumulative = pd.Series([1.0, 1.1, 1.2])
    assert abs(total_return(cumulative) - 0.2) < 1e-9


def test_max_drawdown():
    cumulative = pd.Series([1.0, 2.0, 1.0, 1.5])
    assert abs(max_drawdown(cumulative) - (-0.5)) < 1e-9