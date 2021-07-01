# -*- coding: utf-8 -*-
"""
Created on Mon June 28 17:57:42 2021

@author: Ouoba Mahamadi
"""

import pandas as pd
import yfinance as yf
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

file_name = "Datasets/SUSTAINABILITY_SCORE.xlsx"

sustainability_score = pd.read_excel(file_name)
symbols = sustainability_score['COMPANY TICKER'].sort_values().unique()
st.set_page_config(
    page_title="SUSTAINABILITY SCORE",
    layout="wide")


ticker = st.sidebar.selectbox(
    "Company's TICKER",
     symbols)

mask_for_date = (sustainability_score['COMPANY TICKER'] == ticker)
sustainability_score = sustainability_score.loc[mask_for_date]
date_range = list(sustainability_score['YEAR'])
start_date = st.sidebar.selectbox('Start date', date_range)
end_date = st.sidebar.selectbox('End date', date_range,len(date_range)-1)

if start_date < end_date:
    pass
else:
    st.error('Error: End date must fall after start date.')


mask = (sustainability_score['YEAR'] >= start_date) & (sustainability_score['YEAR'] <= end_date)
sustainability_score_final = sustainability_score.loc[mask]

x_data = sustainability_score_final['SUSTAINABILITY SCORE']    
y_data = sustainability_score_final['YEAR']
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        y=x_data,
        x=y_data,
        name="sustainability score (line)"
    ))

fig.add_trace(
    go.Bar(
        y=x_data,
        x=y_data,
        marker_color='#9ee66e',
        name="Sustainability score (histogram)"
    ))

fig.update_layout(
    title={
        'text': "Company's sustainability score",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

)

fig.update_layout(height=800)

config={
        'modeBarButtonsToAdd': ['drawline']
    }

st.plotly_chart(fig, use_container_width=True, config=config)


