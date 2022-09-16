"""
Created on Wed Sep 7 18:13:31 2022

@author: YASH_SHARMA
"""

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_stock_names')
def get_stock_names():
    response = jsonify({
    'stocks' : util.get_stock_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

@app.route('/predict_stock_price', methods=['POST'])
def predict_stock_price():
    date = request.form['date']
    arr = util.get_estimated_price(date)
    response = jsonify({
        'estimated_price' : str(arr[0][0])
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response



if __name__=="__main__":
    app.run()