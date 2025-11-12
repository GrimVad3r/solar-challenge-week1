# app/main.py

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes
from utils import get_data  # import function from utils.py
import pandas as pd

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="🌞 Solar Data Dashboard", layout="wide")
st.title("🌞 Solar Data Dashboard")

# -----------------------------
# Sidebar: Data & Country Selection
# -----------------------------
st.sidebar.header("Settings")
data_type = st.sidebar.selectbox("Select data type", ['clean', 'raw'])

# Load data with caching
@st.cache_data
def load_data(data_type):
    df = get_data(data_type)
    # Ensure Timestamp is datetime
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

df = load_data(data_type)

if df.empty:
    st.warning("No data loaded! Please check your CSV files or path.")
else:
    st.subheader("Data Preview")
    st.dataframe(df.head(10))

    # -----------------------------
    # Date Range Filter
    # -----------------------------
    if 'Timestamp' in df.columns:
        min_date = df['Timestamp'].min().date()
        max_date = df['Timestamp'].max().date()
        selected_dates = st.sidebar.date_input(
            "Select date range",
            value=[min_date, max_date],
            min_value=min_date,
            max_value=max_date
        )

        if len(selected_dates) == 2:
            start_date, end_date = selected_dates
            df = df[(df['Timestamp'].dt.date >= start_date) & (df['Timestamp'].dt.date <= end_date)]
        else:
            st.warning("Please select a start and end date.")
    else:
        st.sidebar.warning("No 'Timestamp' column found in data.")

    # -----------------------------
    # Country selection
    # -----------------------------
    countries_available = df['Country'].unique()
    selected_countries = st.sidebar.multiselect(
        "Select countries to visualize", options=countries_available, default=countries_available
    )

    if not selected_countries:
        st.warning("Please select at least one country to visualize.")
    else:
        # -----------------------------
        # Mean GHI per Country
        # -----------------------------
        st.subheader("Mean GHI per Country")
        summary_df = df[df['Country'].isin(selected_countries)].groupby('Country')['GHI'].mean().reset_index()

        fig, ax = plt.subplots(figsize=(8,5))
        sns.barplot(data=summary_df, x='Country', y='GHI', palette='Blues', ax=ax)
        ax.set_ylabel("Mean GHI (W/m²)")
        ax.set_title("Mean Global Horizontal Irradiance by Country")
        st.pyplot(fig)
        plt.close(fig)

        # -----------------------------
        # Windrose Charts
        # -----------------------------
        st.subheader("Windrose Charts per Country")
        for country in selected_countries:
            st.write(f"**Windrose - {country}**")
            df_country = df[df['Country'] == country]

            if 'WD' not in df_country.columns or 'WS' not in df_country.columns:
                st.warning(f"Wind data missing for {country}. Skipping...")
                continue

            fig = plt.figure(figsize=(6,6))
            ax = WindroseAxes.from_ax(fig=fig)
            ax.bar(df_country['WD'], df_country['WS'], normed=True, opening=0.8, edgecolor='white')
            ax.set_legend(title="Wind Speed (m/s)")
            plt.title(f"Windrose - {country}")
            st.pyplot(fig)
            plt.close(fig)

        # -----------------------------
        # Correlation Heatmap
        # -----------------------------
        st.subheader("Correlation Heatmap per Country")
        variables = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']

        for country in selected_countries:
            st.write(f"**Correlation Heatmap - {country}**")
            df_country = df[df['Country'] == country]

            missing_cols = [col for col in variables if col not in df_country.columns]
            if missing_cols:
                st.warning(f"Columns {missing_cols} missing for {country}. Skipping...")
                continue

            corr = df_country[variables].corr()
            fig, ax = plt.subplots(figsize=(8,6))
            sns.heatmap(corr, annot=True, fmt='.2f', cmap='viridis', ax=ax)
            ax.set_title(f"Correlation Heatmap - {country}", fontsize=14)
            st.pyplot(fig)
            plt.close(fig)
