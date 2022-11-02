
from distutils.log import debug
from flask import Flask,jsonify,request,render_template
from project_files.utils import DibetesPrediction

import config

app = Flask(__name__)


@app.route("/")  
def hello_flask():
    return render_template("Login.html")
      
        
@app.route('/result', methods = ['POST', 'GET'])

def get_predict():

    if request.method == 'POST':

        result = request.form
        Glucose  = result['Glucose']
        BloodPressure  = result['BP']
        SkinThickness  = result['SkinThickness'] 
        Insulin = result['Insulin']
        BMI = result['BMI']
        DiabetesPedigreeFunction = result['DPF']
        Age = result['Age']

        dib = DibetesPrediction(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        prediction = dib.get_predict()

        return render_template("Login.html", prediction = prediction)

    
        

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 8080)  # server start