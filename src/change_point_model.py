import pymc as pm
import numpy as np


def bayesian_mean_change_point(series):
    """
    Fast Bayesian-style change point model using MAP estimation.
    Suitable for large time series and limited environments.
    """
    y = series.dropna().values
    n = len(y)

    with pm.Model() as model:
        tau = pm.DiscreteUniform("tau", lower=0, upper=n - 1)

        mu_1 = pm.Normal("mu_1", mu=np.mean(y), sigma=np.std(y))
        mu_2 = pm.Normal("mu_2", mu=np.mean(y), sigma=np.std(y))

        sigma = pm.HalfNormal("sigma", sigma=np.std(y))

        mu = pm.math.switch(tau >= np.arange(n), mu_1, mu_2)

        pm.Normal("obs", mu=mu, sigma=sigma, observed=y)

        # MAP estimation instead of full MCMC
        map_estimate = pm.find_MAP()

    return map_estimate
