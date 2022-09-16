from flask import Flask, render_template
from datetime import datetime as dt

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("Index.html",now=dt.now())


if __name__=="__main__":
    app.run()