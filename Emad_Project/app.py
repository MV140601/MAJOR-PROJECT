from flask import Flask,render_template,request
from utility import *


app = Flask(__name__)

@app.route("/",methods=['GET'])

def home():
    return render_template("index.html")

@app.route("/about",methods=['GET'])

def about():
    return render_template("about.html")

@app.route("/working",methods=['GET'])

def working():
    return render_template("working.html")


@app.route("/test",methods=['GET'])

def testPage():
    return render_template('test.html',list=l1,disease='')


@app.route("/calculate",methods=['GET','POST'])

def calculate():
    if request.method=='POST':

        sym1 = request.form['symptom1']
        sym2 = request.form['symptom2']
        sym3 = request.form['symptom3']
        sym4 = request.form['symptom4']
        sym5 = request.form['symptom5']

        l2=[]
        for x in range(0,len(l1)):
            l2.append(0)

        psymptoms = [sym1,sym2,sym3,sym4,sym5]

        for k in range(0,len(l1)):
                for z in psymptoms:
                    if(z==l1[k]):
                        l2[k]=1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(disease[predicted] == disease[a]):
                h='yes'
                break

        if (h=='yes'):
            problem = disease[a]
        else:
            problem = "No disease"

        return render_template("test.html",list=l1,disease=problem)

if __name__=="__main__":
    app.run(debug=True)