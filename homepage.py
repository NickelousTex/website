from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('civic/index.html')

@app.route('/score/', methods = ['POST'])
def predict_page():

    prediction, proba = predict()
    proba0 = np.around(proba[0][0], decimals=5)
    proba1 = np.around(proba[0][1], decimals=5)

    return render_template('predict.html', prediction=prediction[0], proba0=proba0, proba1=proba1)

@app.route('/report/', methods = ['GET'])
def report_page():
    return render_template('workflow.html')

if __name__ == '__main__':
app.run(host='0.0.0.0', port=8000, debug=True)
