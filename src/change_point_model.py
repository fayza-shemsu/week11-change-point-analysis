import pymc as pm
import numpy as np


def bayesian_mean_change_point(series):
    """
    Bayesian single change point model for mean shift.
    """
    y = series.dropna().values
    n = len(y)

    with pm.Model() as model:
        # Change point
        tau = pm.DiscreteUniform("tau", lower=0, upper=n - 1)

        # Priors for means
        mu_1 = pm.Normal("mu_1", mu=np.mean(y), sigma=np.std(y))
        mu_2 = pm.Normal("mu_2", mu=np.mean(y), sigma=np.std(y))

        # Shared noise
        sigma = pm.HalfNormal("sigma", sigma=np.std(y))

        # Piecewise mean
        mu = pm.math.switch(tau >= np.arange(n), mu_1, mu_2)

        # Likelihood
        pm.Normal("obs", mu=mu, sigma=sigma, observed=y)

        trace = pm.sample(1000, tune=1000, chains=2, progressbar=False)

    return trace, tau
