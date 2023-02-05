import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import gzip
from sklearn.model_selection import train_test_split
import joblib
app = Flask(__name__)
with gzip.open('model.pklz', 'rb') as ifp:
    model=pickle.load(ifp)

@app.route('/index',methods = ['POST'])
def predict():
    user_input= request.json
    df=pd.DataFrame(user_input)
    df=df.reindex(columns=col_names)
    predictions=list(model.predict(df))
    if predictions=='0':
        a ="spam"
    else:
        a="Not Spam"
        
    # result=predictions
    return render_template('result.html', result=a)

if __name__ == '__main__':
    model=joblib.load('model.pklz')
    col_names=joblib.load('col_names.pklz')
    app.run(debug=True)