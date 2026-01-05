🍫 Chocolate Rating Predictor

Predict the rating of a chocolate bar based on its characteristics using a machine learning model. This interactive web app allows users to explore chocolate data and get predicted ratings with a polished, user-friendly interface.

Live Demo: Chocolate Rating Predictor

📝 Overview

The Chocolate Rating Predictor predicts chocolate bar ratings (out of 5) using features like:

Company / Maker

Chocolate Bar Name

Cocoa Percentage

Company Location

Bean Type

Broad Bean Origin

Review Year

It is built with Python, Streamlit, and a trained ExtraTrees Regressor model.

⚡ Features

Interactive dropdowns and sliders for selecting chocolate features

Live prediction of chocolate rating

Feature importance visualization for understanding key factors

Dataset statistics and rating histogram in sidebar

Chocolate-themed polished UI

📊 Dataset

The dataset used is flavors_of_cacao.csv, containing chocolate reviews including:

Company / Maker

Specific Bar Name

Cocoa Percentage

Bean Type

Broad Bean Origin

Rating

Review Year

🛠 Built With
Technology	Purpose
Python	Core programming language
Streamlit	Web app framework
scikit-learn	Machine learning model
pandas	Data manipulation
numpy	Numerical computations
matplotlib	Charts and visualizations
🚀 How to Run Locally

Clone the repository

git clone https://github.com/vihashini-18/college-project.git
cd college-project


Create and activate Python environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py

🧠 Model Details

Model: ExtraTreesRegressor

Purpose: Predict chocolate ratings based on multiple features

Handles numerical and categorical data efficiently

Provides feature importance to interpret predictions

📌 Notes

Dropdowns populate from the dataset to ensure valid input values

Predictions are approximate since chocolate ratings are subjective
