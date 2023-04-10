import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 5991293770

def solution(x: np.array, y: np.array) -> bool:
    res = anderson_ksamp([x, y])
    return res.pvalue < 0.07
