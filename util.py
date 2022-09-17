"""
Created on Wed Sep 7 18:01:39 2022

@author: YASH_SHARMA
"""

import pickle
import numpy as np
from datetime import datetime as dt

def get_estimated_price(date):
    ordi = dt.strptime(date,"%Y-%m-%d").date().toordinal()
    model=None
    with open("./artifacts/Final Model.pickle", 'rb') as f:
        model = pickle.load(f)
    pr = model.predict(np.array([ordi]).reshape(-1,1))
    flag=0
    return [pr,flag]     