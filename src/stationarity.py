from statsmodels.tsa.stattools import adfuller, kpss


def adf_test(series):
    """
    Perform Augmented Dickey-Fuller test.
    """
    result = adfuller(series.dropna())
    return {
        "test_statistic": result[0],
        "p_value": result[1],
        "critical_values": result[4]
    }


def kpss_test(series):
    """
    Perform KPSS test.
    """
    statistic, p_value, _, critical_values = kpss(series.dropna(), regression="c")
    return {
        "test_statistic": statistic,
        "p_value": p_value,
        "critical_values": critical_values
    }
