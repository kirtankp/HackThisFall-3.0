import uvicorn
# from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from datasets import dataset
import numpy as np
import pandas as pd

from fastapi import FastAPI
import gzip
# from fastapi import jsonify

import joblib

# model=joblib.load('model.pklz')
# col_names=joblib.load('col_names.pklz')

app = FastAPI()

# pickle_in = pickle.load(open("model.pklz","rb"))
# finalprediction = pickle.load(open("model_predictions.pklz","rb"))

classifier = pickle.load(open('col_names.pklz', 'rb'))

# classifier1=pickle.load(pickle_in)
# classifierfinalpred=pickle.load(finalprediction)

with gzip.open('model.pklz', 'rb') as ifp:
    model=pickle.load(ifp)

@app.get('/')
def index():
    return{'message':'Hello, stranger'}


@app.get('/predict/{text_input}')
def predict(text_input: str):
  
        x=text_input
        # x=x.list()
        v2=x['v2']
        prediction=model.predict([v2])
        if(prediction[0]==0):
            a='Spam Mail'
        else:
            a='Not a Spam Mail'
        return{'a':a }
        
     


if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)