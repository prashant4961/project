import pandas as pd
import numpy as np
import pickle

from flask import Flask, request, jsonify,render_template

app = Flask(__name__)
model = pickle.load(open('ada_modl_hyp.pkl','rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')
    # return "SUCCESS"
@app.route('/subscribed', methods = ['POST'])
def subscribed():

    data = request.form
    vector = np.zeros(33)    
    #df_job,df_marital,df_education,df_contact,df_poutcome
#    `job`
    job = data['job']
    print(job)
    job_list = columns.get('columns')[7:18].tolist()
    print(job_list)
    job_index = job_list.index(job)
    print(job_index)
    
    #  marital
    marital = data['marital']
    print(marital)
    marital_list = columns.get('columns')[18:21].tolist()
    print(marital_list)
    marital_index = marital_list.index(marital)
    print(marital_index)

#   education
    education = data['education']
    print(education)
    education_list = columns.get('columns')[21:28].tolist()
    print(education_list)
    education_index = education_list.index(education)
    print(education_index)

#   contact
    contact = data['contact']
    print(contact)
    contact_list = columns.get('columns')[28:30].tolist()
    print(contact_list)
    contact_index = contact_list.index(contact)
    print(contact_index)

#   poutcome
    poutcome = data['poutcome']
    print(poutcome)
    poutcome_list = columns.get('columns')[30:].tolist()
    print(poutcome_list)
    poutcome_index = poutcome_list.index(poutcome)
    print(poutcome_index)


    vector[job_index] == 1
    vector[marital_index] == 1
    vector[education_index] == 1
    vector[contact_index] == 1
    vector[poutcome_index] == 1
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
   
    
    # return ('customer subscribed  {} > 1=yes >0=no'.format(prediction))
    if prediction[0] == 1:
        final_result = "\ncustomer subscribed"
    else:
        final_result= "\ncustomer not subscribed"

    return render_template('index.html',prediction= final_result)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
