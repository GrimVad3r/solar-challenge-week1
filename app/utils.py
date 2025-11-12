# app/utils.py

import pandas as pd
from pathlib import Path
import streamlit as st

def get_data(data_type='clean'):
    """Load solar data from specified directory"""
    data_dir = Path(__file__).parent.parent / "data"
    
    file_map = {
        'clean': {
            'Benin': 'clean/benin_clean.csv',
            'Togo': 'clean/togo_clean.csv',
            'Sierra Leone': 'clean/sierraleone_clean.csv'
        },
        'raw': {
            'Sierra Leone': 'sierraleone-bumbuna.csv',
            'Togo': 'togo-dapaong_qc.csv',
            'Benin': 'benin-malanville.csv'
        }
    }

    df_list = []
    for country, path in file_map[data_type].items():
        try:
            df_stage = pd.read_csv(
                data_dir / path,
                parse_dates=['Timestamp'] if data_type == 'raw' else None
            )
            df_stage['Country'] = country
            df_list.append(df_stage)
        except FileNotFoundError:
            st.warning(f"File not found: {data_dir / path}")
            continue

    return pd.concat(df_list) if df_list else pd.DataFrame()
