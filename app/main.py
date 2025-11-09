import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_data.csv")

df = load_data()

st.title("Solar KPI Dashboard 🌞")

# --- Widgets ---
countries = st.multiselect("Select Country:", options=df['Country'].unique())
filtered = df[df['Country'].isin(countries)] if countries else df

# --- KPI Example ---
st.header("Key Performance Indicators")
col1, col2 = st.columns(2)
col1.metric("Avg GHI", f"{filtered['GHI'].mean():.2f}")
col2.metric("Avg Temp (Tamb)", f"{filtered['Tamb'].mean():.2f}")

# --- Boxplot ---
st.header("GHI Distribution by Country")
fig = px.box(filtered, x="Country", y="GHI")
st.plotly_chart(fig, use_container_width=True)

# --- Top Regions Table ---
st.header("Top Regions by Avg GHI")
top_regions = filtered.groupby("Region")["GHI"].mean().sort_values(ascending=False).head(10)
st.dataframe(top_regions.reset_index().rename(columns={"GHI": "Avg GHI"}))
