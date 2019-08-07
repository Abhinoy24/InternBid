# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:29:20 2019

@author: TIKI
"""
import pickle

def prediction(data):
    filename = "finalized_model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    filename = "vect.pk"
    loaded_vect = pickle.load(open(filename, 'rb'))
    #Fetch data from csv
    X = data.Data
    indexes = [x for x in range(len(data))]
    X = X.iloc[indexes]
    #Prediction Part
    Pred = loaded_vect.transform(X)
    y_pred2 = loaded_model.predict(Pred)
    return y_pred2
  