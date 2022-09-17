"""
Created on Wed Sep 7 18:13:31 2022

@author: YASH_SHARMA
"""

from flask import Flask, request, jsonify, render_template
import pickle
from datetime import datetime as dt

app = Flask(__name__)

def get_estimated_price(date):
    ordi = dt.strptime(date,"%Y-%m-%d").date().toordinal()
    model=None
    print(ordi)
    with open("./model/Final Model.pickle", 'rb') as f:
        model = pickle.load(f)
    pr = model.predict([[ordi]])[0]
    return pr

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/predict_stock_price', methods=['POST'])
def predict_stock_price():
    date = request.form['date']
    pr = get_estimated_price(date)
    response = jsonify({
        'estimated_price' : str(pr)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__=="__main__":
    app.run()