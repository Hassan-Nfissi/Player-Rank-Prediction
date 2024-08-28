# Player Rank Prediction

This project focuses on predicting the rank of Premier League players using machine learning, specifically leveraging the Scikit-learn framework. The model is trained on a dataset that contains detailed statistics of Premier League players, sourced from Kaggle. The dataset includes features such as player name, team, games played, goals, assists, and other relevant performance metrics. The primary objective is to build an accurate predictive model that can estimate a player's rank based on these statistics.

## Table of Contents
- [Project Overview](#project-overview)
- [Alorithm Used](#algorithm-used)
- [Dataset](#dataset)
- [Usage](#Usage)
- [File Structure](#File Structure)
- [Deployment](#Deployment)
## Project Overview

In the sports industry, accurately predicting a player's rank is essential for teams, coaches, and analysts to make informed decisions. This project employs machine learning techniques to predict player ranks based on their performance metrics. The main steps include:

- **Data Collection and Preprocessing**: Collect and preprocess data from Kaggle, including cleaning and feature engineering.
- **Exploratory Data Analysis (EDA)**: Perform EDA to identify key features, correlations, and insights that will influence the model.
- **Model Selection and Training**: Choose and train machine learning models such as Linear Regression, Decision Trees, or Random Forest.
- **Model Evaluation**: Evaluate model performance using metrics like Mean Squared Error (MSE), R-squared, or others relevant to the chosen model.
- **Rank Prediction on New Data**: Use the trained model to predict player ranks based on new input data.
## Algorithm Used
The model used in this project is a **Decision Tree**. 

- **Decision Tree**: This model is chosen for its interpretability and ability to handle both categorical and numerical data. It works by recursively splitting the dataset based on feature values to make predictions about the player's rank. Decision Trees are advantageous because they can capture non-linear relationships and interactions between features, making them a powerful choice for this type of predictive task.

The Decision Tree model was trained on the dataset containing player statistics and was evaluated using metrics such as Mean Squared Error (MSE) and R-Squared to ensure accuracy and reliability.
## Dataset

The dataset used in this project contains comprehensive statistics of Premier League players, including:

- **Player Name:** The name of the player.
- **Team:** The team the player belongs to.
- **Games Played (GP):** Total number of games played.
- **Games Started (GS):** Total number of games started.
- **Minutes Played (MIN):** Total minutes played by the player.
- **Goals (G):** Total goals scored.
- **Assists (ASST):** Total assists made.
- **Shots (SHOTS):** Total number of shots taken.
- **Shots on Goal (SOG):** Total shots that were on target.

You can download the dataset from [Kaggle](https://www.kaggle.com) or use any other relevant sports dataset.

## Usage
* First browse to the folder containing the project:
`cd player-rank-prediction`
* Installing the requirement :
`pip install -r requirements.txt`
* Then you should launch the app in a terminal.
`python app.py`

* And finally, through the terminal you will get a link to your application. By default it's : http://127.0.0.1:5000/.
## File Structure
## Deployment
This project has been deployed using a Flask web application, allowing users to interact with the model through a web interface. The deployment process involved:
* **Web Interface**: The user interface is built with HTML, CSS, and JavaScript to allow users to input player data and get predictions.
* **Flask Backend**: The Flask framework is used to handle requests, process inputs, and return the predicted player ranks.
* **Dockerization**: The entire application is containerized using Docker, making it easy to deploy and run on different environments.
* **Azure Deployment**: The Docker container is deployed on Azure, making the application accessible over the web. Azure’s services ensure scalability and reliability of the deployed model.
## Screenshots"# Player-Rank-Prediction" 
