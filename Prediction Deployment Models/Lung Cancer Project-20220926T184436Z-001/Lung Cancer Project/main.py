from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


# machine learning 

def PredictBC(data):
    model = pickle.load(open('breast-dataset/model.pkl', 'rb')) #binary read
    pred = model.predict([data])
    if pred[0]==2:
        pred = 'Benign'
    else:
        pred = 'Malignant'
    return pred

def PredictLC(data):
    model = pickle.load(open('lung-dataset/lung_reg.sav','rb'))
    pred = model.predict([data])
    pred = pred[0]*100 #percentage mei convert karne ke liye
    return str(pred)+'%' #formatting ke liye 


def PredictPC(data):
    model = pickle.load(open('prostate-dataset/prostate.sav','rb'))
    pred = model.predict([data])
    pred = pred[0]*100
    return str(pred)+'%'


# routes 

@app.route('/') #jo hum alag alag pages mei jaate hai unke liye we use routes
def index():
    title = 'Cancer Prediction'
    return render_template("home.html",title=title)


@app.route('/team')
def team():
    title = 'Team'
    return render_template("team.html",title=title)




@app.route('/breastcancer')
def breastCancer():
    title = 'Breast Cancer'
    
    return render_template("index.html", title=title)

@app.route('/lungcancer')
def lungCancer():
    title = 'Lung Cancer'
    return render_template("index2.html", title=title)

@app.route('/prostateCancer')
def prostateCancer():
    title = 'Prostate Cancer'
    return render_template("index3.html", title = title)




# processing the data from the webpages

@app.route('/lungresult', methods=  ["POST"])
def lungResult():
    title = 'Prediction'
    data = []
    try:
        q = ''
        q = (request.form.get('gender'))
        if q=='F':
            data.append(0)
        elif q=='M':
            data.append(1)
        else:
            return render_template('invalid.html',title=title,output='Invalid Gender')
        data.append(int(request.form.get('age')))
        data.append(int(request.form.get('smoking')))
        data.append(int(request.form.get('yellow_fingers')))
        data.append(int(request.form.get('anxiety')))
        data.append(int(request.form.get('peer_pressure')))
        data.append(int(request.form.get('chronic_disease')))
        data.append(int(request.form.get('fatigue')))
        data.append(int(request.form.get('allergy')))
        data.append(int(request.form.get('wheezing')))
        data.append(int(request.form.get('alcohol_consuming')))
        data.append(int(request.form.get('coughing')))
        data.append(int(request.form.get('shortness_of_breath')))
        data.append(int(request.form.get('swallowing_difficulty')))
        data.append(int(request.form.get('chest_pain')))
        print(data)
        output = PredictLC(data)
        return render_template("lungPredict.html", title=title,output = output ) #render template se hum puri html file browser ko bhej dete hai, output jo aaya hai we will use it in html file
    except:
        return render_template('invalid.html',title=title,output='Invalid data format')



# @app.route('/breastResult',methods = ["POST"])
# def breastResult():
#     title = 'Prediction'
#     data = []
#     for i in range(0,len(breastCancerCols)):
#         info = request.form.get(breastCancerCols[i])
#         print(info)
#         if info.isdigit:
#              data.append(int(info))
#         print(data)
#     try:
#         data.append(int(request.form.get('clump_thickness')))
#         data.append(int(request.form.get('uniform_cell_size')))
#         data.append(int(request.form.get('uniform_cell_shape')))
#         data.append(int(request.form.get('marginal_adhesion')))
#         data.append(int(request.form.get('single_epithelial_size')))
#         data.append(int(request.form.get('bare_nuclei')))
#         data.append(int(request.form.get('bland_chromatin')))
#         data.append(int(request.form.get('normal_nucleoli')))
#         data.append(int(request.form.get('mitoses')))

#         output = PredictBC(data)

#         return render_template("breastPredict.html", title=title,output = output) 
#     except:
#         return render_template("invalid.html", title=title, output=  'Invalid data format')

# @app.route('/prostateResult', methods = ["POST"])
# def prostateResult():
#     title = 'Prediction'
#     data = []
#     try: 
#         data.append(int(request.form.get('radius')))
#         data.append(int(request.form.get('texture')))
#         data.append(int(request.form.get('perimeter')))
#         data.append(int(request.form.get('area')))
#         data.append(float(request.form.get('smoothness')))
#         data.append(float(request.form.get('compactness')))
#         data.append(float(request.form.get('symmetry')))
#         data.append(float(request.form.get('fractal_dimension')))
#         output = PredictPC(data)
#         return render_template("prostatePredict.html", title=title,output = output )
#     except:
#         return render_template("invalid.html",title=title,output="Invalid data format")

    

# driver code 

if __name__ == '__main__':  # to make sure that unexpected server run are not there
    app.run(debug=True)