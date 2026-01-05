🍫 Chocolate Rating Predictor

Predict chocolate bar ratings using machine learning.
A fully interactive Streamlit web app that allows users to explore and predict chocolate ratings based on cocoa content, company, bean type, and origin.

Live Demo: https://college-project-mbf6jkf9xyagbjqtgswfwt.streamlit.app/

🏆 Key Features

Predict Chocolate Ratings: Enter chocolate details to get a predicted rating (0–5 scale).

Interactive UI: Dropdowns populated from real dataset values, slider for cocoa percentage.

Feature Insights: Visualize top 5 features influencing the prediction.

Dataset Overview: Sidebar histogram showing rating distribution.

Deployment Ready: Fully functional on Streamlit Cloud.

🛠 Technology Stack
Technology	Purpose
Python	Core programming language
Streamlit	Web app UI & interactivity
scikit-learn	Machine learning model (ExtraTreesRegressor)
Pandas	Data handling & preprocessing
NumPy	Numerical operations
Matplotlib	Visualization of distributions and feature importance
📊 Dataset

The app uses the Flavors of Cacao dataset, containing:

Company / Maker

Specific Bar Name

Cocoa Percentage

Company Location

Bean Type

Broad Bean Origin

Review Year

Rating

Dataset is included in the repository as flavors_of_cacao.csv.

⚙️ How It Works

Load and preprocess the dataset (handle missing values, encode categorical features).

Train an ExtraTreesRegressor model on the dataset.

Provide interactive inputs in the Streamlit sidebar.

Predict rating and display top features influencing the prediction.

💻 Installation & Local Run

Clone the repository

git clone https://github.com/vihashini-18/college-project.git
cd college-project


Create a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py

📈 Model Details

Model: ExtraTreesRegressor

Reason for Choice: Handles nonlinear relationships and categorical variables effectively, provides feature importance insights, robust for tabular datasets.

Performance: Predicts ratings reasonably; subjective nature of ratings may introduce variance.

🎨 UI & User Experience

Dropdowns populated from dataset for accurate input selection.

Slider for cocoa content to allow precise input.

Feature importance chart helps understand what drives the predicted rating.

Chocolate-themed color scheme for intuitive UX.
