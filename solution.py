import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 5991293770

def solution(x: np.array, y: np.array) -> bool:
    _, pvalue = ks_2samp(x, y)
    return pvalue < 0.07
