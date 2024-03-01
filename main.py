from wsgiref import simple_server

import requests
from flask import Flask, request, render_template
from flask import Response
import flask_monitoringdashboard as dashboard
import pandas as pd
import os
from flask_cors import CORS, cross_origin
import orjson
from test import get_testData

app = Flask(__name__)
#dashboard.bind(app)
CORS(app)

@app.route('/', methods=['POST','GET'])
def index_page():
    return render_template('index.html')

@app.route('/predictions')
@cross_origin()
def get_allData():
    #zp=get_testData()
    #return render_template("index.html")
    dr=pd.read_csv("C:\\Users\\MCS\\Downloads\\diabetes.csv")
    temp = dr.loc[:, ["Pregnancies", "Glucose", "Insulin", "Age"]].to_json(orient='records')
    temp=orjson.loads(temp)
    #return render_template("index.html",ctrsuccess=temp)
    return temp



if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=3000)