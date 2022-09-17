"""
Created on Wed Sep 7 18:01:39 2022

@author: YASH_SHARMA
"""

import pickle
import numpy as np
from datetime import datetime as dt

def get_estimated_price(date):
    print(date)
    ordi = dt.strptime(date,"%Y-%m-%d").date().toordinal()
    model=None
    print(ordi)
    with open("./model/Final Model.pickle", 'rb') as f:
        model = pickle.load(f)
    pr = model.predict([[ordi]])
    flag=0
    print(pr)
    return [pr,flag]