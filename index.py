from flask import Flask, render_template
import csv
from sklearn import model_selection

app = Flask(__name__)

@app.route('/')
def starpage():
    return render_template('google-analytics-revenue-prediction.html')


@app.route('/predict', methods=['POST'])
def predict():
    with open('submission.csv', 'r') as fichier:
        lecteur_csv = csv.reader(fichier)
        data = list(lecteur_csv)

    # Effectuer la prédiction en utilisant votre modèle
    prediction = model_selection.predict(data)
    print(prediction)

    # Retourner la prédiction sous forme de réponse JSON
    # return jsonify(prediction)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)