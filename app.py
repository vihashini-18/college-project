# app.py
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="🍫 Chocolate Rating Predictor",
    page_icon=":chocolate_bar:",
    layout="wide"
)

st.title("🍫 Chocolate Rating Predictor")
st.markdown("Predict the rating of a chocolate bar based on its features!")

# -----------------------------
# Load dataset (relative path!)
# -----------------------------
df_ui = pd.read_csv("flavors_of_cacao.csv")  # relative path for deployment

# Rename columns
df_ui.columns = ['Company', 'BarName', 'REF', 'ReviewDate', 'CocoaPercent', 
                 'CompanyLocation', 'Rating', 'BeanType', 'BroadBeanOrigin']

# Clean CocoaPercent
df_ui['CocoaPercent'] = df_ui['CocoaPercent'].str.replace('%','', regex=False).astype(float)

# -----------------------------
# Prepare training data
# -----------------------------
df_train = df_ui.copy()

num_cols = ['CocoaPercent', 'ReviewDate', 'REF']
cat_cols = ['Company', 'BarName', 'CompanyLocation', 'BeanType', 'BroadBeanOrigin']

# Impute missing values
num_imputer = SimpleImputer(strategy='median')
cat_imputer = SimpleImputer(strategy='most_frequent')

df_train[num_cols] = num_imputer.fit_transform(df_train[num_cols])
df_train[cat_cols] = cat_imputer.fit_transform(df_train[cat_cols])

# Encode categorical for model
encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
df_train[cat_cols] = encoder.fit_transform(df_train[cat_cols])

# Train model
X = df_train.drop('Rating', axis=1)
y = df_train['Rating']
model = ExtraTreesRegressor(n_estimators=500, max_depth=15, random_state=42, n_jobs=-1)
model.fit(X, y)

# -----------------------------
# Sidebar: Dataset stats
# -----------------------------
st.sidebar.title("🍫 Dataset Overview")
st.sidebar.write(f"Number of chocolate bars: {df_ui.shape[0]}")
st.sidebar.write(f"Number of features: {df_ui.shape[1]-1}")

# Rating histogram
fig, ax = plt.subplots(figsize=(4,3))
ax.hist(df_ui['Rating'], bins=20, color='#7B3F00', alpha=0.8)
ax.set_xlabel('Rating')
ax.set_ylabel('Count')
st.sidebar.pyplot(fig)

# -----------------------------
# Dropdown options sorted by popularity
# -----------------------------
def sorted_by_popularity(col):
    return df_ui[col].value_counts().index.tolist()

company_options = sorted_by_popularity('Company')
bar_options = sorted_by_popularity('BarName')
location_options = sorted_by_popularity('CompanyLocation')
bean_options = sorted_by_popularity('BeanType')
broad_options = sorted_by_popularity('BroadBeanOrigin')

# -----------------------------
# User Input Form
# -----------------------------
with st.form("choco_form"):
    st.subheader("Enter Chocolate Details")
    company = st.selectbox("Company", company_options)
    barname = st.selectbox("Bar Name", bar_options)
    cocoa = st.slider("Cocoa Percent (%)", 30, 100, 70)
    location = st.selectbox("Company Location", location_options)
    bean_type = st.selectbox("Bean Type", bean_options)
    broad_origin = st.selectbox("Broad Bean Origin", broad_options)
    review_date = st.number_input("Review Year", min_value=1900, max_value=2026, value=2015)

    submitted = st.form_submit_button("Predict Rating")

# -----------------------------
# Prediction
# -----------------------------
if submitted:
    input_df = pd.DataFrame({
        'Company':[company],
        'BarName':[barname],
        'REF':[0],
        'ReviewDate':[review_date],
        'CocoaPercent':[cocoa],
        'CompanyLocation':[location],
        'BeanType':[bean_type],
        'BroadBeanOrigin':[broad_origin]
    })

    # Impute & encode for model
    input_df[num_cols] = num_imputer.transform(input_df[num_cols])
    input_df[cat_cols] = cat_imputer.transform(input_df[cat_cols])
    input_df[cat_cols] = encoder.transform(input_df[cat_cols])

    # Predict
    pred = model.predict(input_df)[0]
    st.success(f"Predicted Chocolate Rating: **{pred:.2f} / 5**")
    st.balloons()

# -----------------------------
# Feature Importance
# -----------------------------
st.subheader("🌟 Top 5 Feature Importances")
importances = model.feature_importances_
feat_imp = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feat_imp = feat_imp.sort_values(by='Importance', ascending=False).head(5)

fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.barh(feat_imp['Feature'], feat_imp['Importance'], color='#D2691E', alpha=0.8)
ax2.set_xlabel('Importance')
ax2.set_ylabel('Feature')
st.pyplot(fig2)
