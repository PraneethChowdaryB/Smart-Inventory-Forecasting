import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
from io import StringIO

# Database connection parameters
db_params = {
    "host": "your_host",
    "database": "your_db",
    "user": "your_user",
    "password": "your_password",
    "port": 5432  # Ensure this is an integer value, e.g., 5432 for PostgreSQL
}

# Function to connect to the database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=db_params["host"],
            database=db_params["database"],
            user=db_params["user"],
            password=db_params["password"],
            port=db_params["port"]
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Function to load data from the database
def load_data_from_db():
    conn = connect_to_db()
    if conn:
        query = "SELECT * FROM your_table;"  # Replace with your actual query
        data = pd.read_sql(query, conn)
        conn.close()
        return data
    else:
        return None

# Function to load CSV data
def load_csv_data(uploaded_file):
    data = pd.read_csv(uploaded_file)
    return data

# Title and Introduction
st.title("📊 Inventory Forecasting Dashboard")
st.markdown("""
    Welcome to the **Smart Inventory Forecasting Dashboard**! 
    This platform helps businesses analyze sales data, predict demand, and make data-driven inventory decisions.
""")

# Upload Sales Data (CSV) or Load Data from Database
uploaded_file = st.file_uploader("📂 Upload Sales Data (CSV)", type=["csv"])

if uploaded_file is not None:
    data = load_csv_data(uploaded_file)
    st.write("Data uploaded successfully!")
else:
    st.write("No file uploaded. Loading data from the database...")
    data = load_data_from_db()

# Check if data is loaded
if data is not None:
    st.subheader("📋 Sample Data")
    st.write(data.head(10))

    # Data visualization
    st.subheader("📈 Sales Trend Over Time")
    if 'date' in data.columns and 'sales' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
        plt.figure(figsize=(10, 6))
        plt.plot(data['date'], data['sales'], label="Sales")
        plt.title("Sales Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.legend()
        st.pyplot(plt)
    else:
        st.error("The data should contain 'date' and 'sales' columns.")

    # Seasonal Trends (Monthly)
    if 'date' in data.columns and 'sales' in data.columns:
        data['month'] = data['date'].dt.month
        monthly_sales = data.groupby('month')['sales'].sum()
        st.subheader("📅 Seasonal Trends (Monthly Sales)")
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='orange')
        plt.title("Monthly Sales Trends")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        st.pyplot(plt)

    # Forecast (Dummy for now)
    st.subheader("📅 Sales Forecasting (Dummy Data)")
    forecast_data = pd.DataFrame({
        'date': pd.date_range(start=data['date'].max(), periods=30, freq='D'),
        'forecasted_sales': [data['sales'].mean()] * 30  # Dummy forecast using the mean sales
    })
    st.write(forecast_data)

    # Display forecast
    st.subheader("📊 Forecasted Sales Data")
    st.write(forecast_data)

else:
    st.error("No data available to display. Please upload a CSV file or check your database connection.")

