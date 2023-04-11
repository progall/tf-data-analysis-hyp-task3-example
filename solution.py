import pandas as pd
import numpy as np
from scipy.stats import pareto, cauchy, norm, ttest_ind, ks_2samp, mannwhitneyu, permutation_test

chat_id = 322172960 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    y = []
    
    for хlst in х:
        if xlt > 300:
            y.append(300)
        else
            y.append(xlt)
            
    return ttest_ind(x, y, equal_var=False, alternative="greater").pvalue < 0.04 # Ваш ответ, True или False
