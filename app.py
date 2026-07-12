import streamlit as st
import pandas as pd
import pickle
# Load Model
from pathlib import Path
import pickle

MODEL_PATH = Path(__file__).parent / "real_estate_price_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
# model = pickle.load(open("real_estate_price_model.pkl", "rb"))

# Load Dataset
df = pd.read_csv("Bengaluru_House_Data.csv")

# Data Cleaning same as training

df = df.drop(['area_type','availability','society','balcony'], axis=1)
df = df.dropna()
df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]))
df.drop('size', axis=1, inplace=True)


def convert_sqft(x):
    try:
        if '-' in str(x):
            a = x.split('-')
            return (float(a[0]) + float(a[1])) / 2
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df.dropna(inplace=True)
location_count = df.location.value_counts()
location_less_10 = location_count[location_count <= 10]
df.location = df.location.apply(
    lambda x: "Other" if x in location_less_10 else x
)
locations = sorted(df.location.unique())


# UI

st.title("🏡 Real Estate Price Prediction")

st.write("Enter Property Details")

location = st.selectbox("📍 Location", locations)

sqft = st.number_input(
    "Total Square Feet",
    min_value=300,
    max_value=30000,
    value=1200
)

bath = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

bhk = st.number_input(
    "BHK",
    min_value=1,
    max_value=10,
    value=2
)


# Prediction

if st.button("💰 Predict Price"):

    x = pd.DataFrame(
        columns=model.feature_names_in_
    )

    x.loc[0] = 0

    x["total_sqft"] = sqft
    x["bath"] = bath
    x["bhk"] = bhk

    location_column = "location_" + location

    if location_column in x.columns:
        x[location_column] = 1

    prediction = model.predict(x)[0]

    st.success(
        f"Estimated House Price : ₹ {prediction:.2f} Lakhs"
    )
