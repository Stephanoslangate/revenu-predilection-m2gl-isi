from flask import Flask, render_template,request, redirect,jsonify


app = Flask(__name__)

@app.route('/')
def starpage():
    #print('The scikit-learn version is {}.'.format(sklearn.__version__))
    return render_template('google-analytics-revenue-prediction.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
        return "Success"
    # Retourner la prédiction sous forme de réponse JSON
    #return jsonify(prediction)
    
if __name__ == '__main__':
    app.run()