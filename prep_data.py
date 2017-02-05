"""
Functions for preparing data
"""

import numpy as np
import pandas as pd


def get_col_vals(df, col1, col2):
    """
    Get column values 
    """
    y1 = np.array(df[col1])
    y2 = np.array(df[col2])
    return y1, y2


def prep_data(df, col1, col2):
    """
    Prepare data for pymc3 and return mean mu and sigma
    """
    y1 = np.array(df[col1])
    y2 = np.array(df[col2])

    y = pd.DataFrame(dict(value=np.r_[y1, y2], 
                        group=np.r_[[col1]*len(y1), 
                        [col2]*len(y2)]))

    mu = y.value.mean()
    sigma = y.value.std() * 2

    return y, mu, sigma
