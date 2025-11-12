# app/main.py

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from app.utils import get_data  # import function from utils.py

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🌞 Solar Data Dashboard")

# Sidebar: select data type
data_type = st.sidebar.selectbox("Select data type", ['clean', 'raw'])

# Load data
df = get_data(data_type)

if df.empty:
    st.warning("No data loaded! Please check your CSV files or path.")
else:
    st.subheader("Data Preview")
    st.dataframe(df.head(10))

    # Example chart: mean GHI per country
    st.subheader("Mean GHI per Country")
    summary_df = df.groupby('Country')['GHI'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(data=summary_df, x='Country', y='GHI', palette='skyblue', ax=ax)
    ax.set_ylabel("Mean GHI")
    ax.set_title("Mean Global Horizontal Irradiance by Country")
    st.pyplot(fig)

    # Optional: full data table
    st.subheader("Full Data Table")
    st.dataframe(df)
