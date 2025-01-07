
# Smart Inventory Forecasting Dashboard

## Overview
The **Smart Inventory Forecasting Dashboard** is a data engineering project designed to help businesses analyze sales data, predict demand, and make informed inventory decisions. This dashboard provides a user-friendly interface to visualize historical sales trends, forecast future demand, and gain actionable insights for inventory management.

## Purpose of the Project
In today’s competitive market, managing inventory effectively is crucial for reducing costs and maximizing profitability. This project was created to:

1. **Enhance Decision-Making**: Provide businesses with accurate sales forecasts to make data-driven inventory decisions.
2. **Reduce Wastage**: Avoid overstocking and understocking by understanding demand patterns.
3. **Simplify Analysis**: Deliver a simple yet powerful tool for visualizing and interpreting sales data without requiring advanced technical skills.
4. **Enable Scalability**: Lay the foundation for integrating advanced analytics and machine learning models in the future.

## Features
- **Upload Sales Data**: Easily upload sales data in CSV format.
- **Historical Trends**: Visualize historical sales trends across different stores and products.
- **Demand Forecasting**: Predict future sales trends using forecast data.
- **Seasonality Insights**: Analyze seasonal patterns to prepare for peak and off-peak periods.
- **Top Products Analysis**: Identify top-performing products to optimize stock levels.
- **Interactive Filters**: Filter data by store or product for detailed analysis.
- **Database Integration**: Support for PostgreSQL to store and fetch sales data.

## Getting Started

### Prerequisites
Ensure you have Python 3.8 or higher installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/PraneethChowdaryB/Smart-Inventory-Forecasting
   cd smart-inventory-forecasting
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database connection (if using a database). Update the database parameters in `dashboard.py`:
   ```python
   db_params = {
       "host": "your_host",
       "database": "your_db",
       "user": "your_user",
       "password": "your_password",
       "port": 5432
   }
   ```

### Running the Dashboard
1. Run the Streamlit app:
   ```bash
   streamlit run dashboard.py
   ```
2. Open the URL provided by Streamlit in your browser to access the dashboard.

## Files in the Repository
- **dashboard.py**: Streamlit application for the inventory forecasting dashboard. This file contains the core logic for uploading sales data, visualizing trends, and predicting future demand using forecasted data.
- **initial_smart_inventory_analytics.ipynb**: Jupyter Notebook that demonstrates the initial data exploration, data cleaning, and preparation of the dataset. This includes steps to preprocess sales data and analyze basic trends.
- **train.csv**: A sample dataset containing historical sales records to test the dashboard's functionality.
- **simulated_data.csv**: A simulated dataset for testing the forecasted sales visualization.
- **requirements.txt**: A list of all dependencies and libraries required to run the project.

## Project Workflow
1. **Data Exploration (Jupyter Notebook)**:
   - The notebook `initial_smart_inventory_analytics.ipynb` provides an in-depth exploration of the sales dataset.
   - Key steps include handling missing data, analyzing trends, and generating summary statistics.

2. **Dashboard Development (Streamlit)**:
   - `dashboard.py` is the main script for the dashboard. It allows users to:
     - Upload and visualize their sales data.
     - Fetch historical data from a database.
     - Analyze sales trends and seasonality.
     - View demand forecasts.

3. **Sample Data**:
   - `train.csv` and `simulated_data.csv` provide users with example datasets to test the dashboard.

## Benefits
- **Improved Inventory Management**: Ensure adequate stock levels for high-demand products.
- **Cost Reduction**: Minimize storage and operational costs by avoiding overstocking.
- **Increased Sales**: Align inventory with customer demand, leading to higher sales.
- **Data-Driven Insights**: Leverage sales data to identify trends and opportunities.

## Future Improvements
- **Enhanced Forecasting Models**: Integrate advanced machine learning models to improve forecast accuracy.
- **Real-Time Data Integration**: Enable real-time data streaming from APIs or databases.
- **User Authentication**: Add authentication for secure and personalized user experiences.
- **Visualization Enhancements**: Provide more interactive and customizable charts.
- **Scalability**: Deploy the dashboard on cloud platforms like AWS or Azure for better accessibility and performance.

## About the Author
This project was developed by **Sai Praneeth Bethapudi** as a part of a data engineering learning initiative to gain hands-on experience in creating real-world applications. The goal was to apply data processing and visualization skills to solve practical business challenges.
