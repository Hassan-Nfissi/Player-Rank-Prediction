import json
from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)

with open('model/model (1).pickle', 'rb') as file:
    model = pickle.load(file)

# Charger les données de l'équipe
with open('model/team.json', 'rb') as file:
    team1 = json.load(file)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=["POST"])
def predict():
    team_cat = request.form['team']
    team = team1[team_cat]
    GB = int(request.form['gp'])
    gs = int(request.form['gs'])
    min_played = int(request.form['min'])
    goals = int(request.form['g'])
    assists = int(request.form['asst'])
    shots = int(request.form['shots'])
    sog = int(request.form['sog'])

    features = np.array([[team, GB, gs, min_played, goals, assists, shots, sog]])

    pred = int(model.predict(features)[0])

    return str(pred)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
