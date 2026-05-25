import streamlit as st
import sqlite3
import pandas as pd
import os

# --- Page config ---
st.set_page_config(
    page_title="Weather ETL Dashboard",
    page_icon="🌤️",
    layout="wide"
)

# --- Load data from SQLite ---
DB_PATH = os.path.join("data", "weather.db")

@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM weather_forecast", conn)
    conn.close()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

# --- App ---
st.title("🌤️ Weather ETL Pipeline Dashboard")
st.caption("Data pulled from Open-Meteo API · Honolulu, HI · 7-day forecast")

# Load the data
df = load_data()

# --- Metric cards (top row) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Avg Temperature", f"{df['temperature_f'].mean():.1f} °F")
with col2:
    st.metric("Max Temperature", f"{df['temperature_f'].max():.1f} °F")
with col3:
    st.metric("Avg Humidity", f"{df['humidity_pct'].mean():.1f} %")
with col4:
    st.metric("Avg Wind Speed", f"{df['wind_speed_mph'].mean():.1f} mph")

st.divider()

# --- Temperature chart ---
st.subheader("Temperature over the next 7 days (°F)")
st.line_chart(df.set_index("timestamp")["temperature_f"])

# --- Humidity chart ---
st.subheader("Humidity over the next 7 days (%)")
st.line_chart(df.set_index("timestamp")["humidity_pct"])

# --- Wind speed chart ---
st.subheader("Wind speed over the next 7 days (mph)")
st.line_chart(df.set_index("timestamp")["wind_speed_mph"])

st.divider()

# --- Comfort breakdown ---
st.subheader("Hours by comfort level")
comfort_counts = df["comfort"].value_counts().reset_index()
comfort_counts.columns = ["Comfort level", "Hours"]
st.bar_chart(comfort_counts.set_index("Comfort level"))

# --- Raw data table ---
st.subheader("Raw data")
st.dataframe(df, use_container_width=True)