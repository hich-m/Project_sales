import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_random_sales(min_val, max_val, size):
    """
    Generate a NumPy array of random integers between min_val and max_val.
    size: number of values (e.g., 12 months)
    """
    return np.random.randint(min_val, max_val + 1, size)

def generate_dates():
    return pd.date_range(start='2025-01-01', end='2025-12-01', freq='MS')

