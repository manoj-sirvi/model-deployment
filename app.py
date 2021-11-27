import os
from flask import Flask, render_template, request, url_for, redirect
import json
from data.sipp_policies.sipp_policies import return_sipp

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/ViewSiPP', methods = ['POST', 'GET'])
def sipp():
    if request.method == 'POST': 
        policy_req = request.form['policy_req']
        sipp_pol_final = return_sipp(policy_req)
        op_json = json.dumps(sipp_pol_final)
        print('op_json'+str(type(op_json)))
        return render_template('sipp_op.html', op_json = op_json)
    return render_template("ViewSiPP.html")

@app.route('/guide')
def guide(): 
    return render_template('guide.html')

@app.route('/viewPolicy')
def view_policy(): 
    return render_template('viewPolicy.html')

if __name__ == "__main__": 
    app.run()
