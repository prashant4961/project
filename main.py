import pandas as pd
import numpy as np
import pickle

from flask import Flask, request, jsonify

app = Flask(__name__)
model = pickle.load(open('ada_modl_hyp.pkl','rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

@app.route('/subscribed', methods = ['POST'])
def subscribed():

    data = request.form
    vector = np.zeros(33)

    location = data['location']
    print(location)
    location_list = columns.get('columns')[8:].tolist()
    print(location_list)
    location_index = location_list.index(location)
    print(location_index)

    vector[location_index] == 1
    vector[0] = data['age']
    vector[1] = data['default']
    vector[3] = data['housing']
    vector[4] = data['loan']
    vector[5] = data['duration']
    vector[6] = data['campaign']
    vector[7] = data['pdays']
    vector[8] = data['previous']



    input = [vector]

    prediction = model.predict(input)
    if prediction == 1:
        print("has the client subscribed a term deposit? >>>>> YES")
    else:
        
        return ('has the client subscribed a term deposit? >>>>> NO')

if __name__ == "__main__":
    app.run(debug=True)
