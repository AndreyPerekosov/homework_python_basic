import json

import pandas as pd
import numpy as np


def calc(df, num_of_porto: int, risk_rate: int) -> dict:

    NUM_PORTFOLIOS = num_of_porto
    RISK_FREE_RATE = risk_rate
    # annual average return
    av_ret = df.pct_change().mean() * 12
    # covariance matrix
    cov_matrix = df.pct_change().cov()
    # lists of data
    p_returns = []
    p_vol = []
    p_weights = []
    num_assets = len(df.columns)
    for portfolio in range(NUM_PORTFOLIOS):
        weights = np.random.random(num_assets)
        weights = weights / np.sum(weights)
        p_weights.append(weights)
        returns = np.dot(weights, av_ret)
        p_returns.append(returns)
        var = cov_matrix.mul(weights, axis=0).mul(weights, axis=1).sum().sum()
        std = np.sqrt(var)
        # annual std dev
        std *= np.sqrt(12)
        p_vol.append(std)
    data = {'Returns': p_returns, 'Volatility': p_vol}
    for counter, symbol in enumerate(df.columns.tolist()):
        data[symbol + " weight"] = [w[counter] for w in p_weights]
    portfolios = pd.DataFrame(data)
    optimal_porto = portfolios.iloc[((portfolios['Returns'] - RISK_FREE_RATE) / portfolios['Volatility']).idxmax()]
    result = {'Sharp': (optimal_porto['Returns'] - RISK_FREE_RATE) / optimal_porto['Volatility'],
              'data': optimal_porto.drop(['Returns', 'Volatility'], axis=0).to_dict(),
              'vol_ret': optimal_porto[['Returns', 'Volatility']].to_dict()
              }
    return result


def colors(colors_num):
    with open('data/colors.json') as f:
        data = json.load(f)
        for i in range(colors_num):
            t = tuple(data[i]['rgb'])
            yield f'rgb{t}'

