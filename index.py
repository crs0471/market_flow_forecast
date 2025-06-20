import streamlit as st
from scrap_news import financial_express
from gemini_api import analyze_news
import pandas as pd


st.set_page_config(
    "Market Forecast",
    layout="wide"
)

all_news = financial_express()
st.title("Market Forecast")
col1, col2 = st.columns(2)

with st.container(border=True, height=300):
    st.write("Forecast : ")
    
    forecast = analyze_news(all_news) 
    if forecast.startswith("```json") : forecast = forecast[7:]
    if forecast.endswith("```") : forecast = forecast[:-3]
    forecast = eval(forecast)   
    forecast = pd.DataFrame(forecast)
    forecast['forecast'] = forecast['forecast'].apply(lambda x : {"Up":"Up ✅", "Down": "Down ❌", "Neutral": "Neutral ⚖️"}[x])
    styled_df = forecast.style.set_table_styles([
        {'selector': 'th.col0', 'props': [('min-width', '120px')]},
        {'selector': 'th.col1', 'props': [('min-width', '80px')]},
        {'selector': 'th.col2', 'props': [('min-width', '200px')]}
    ])

    st.dataframe(styled_df, use_container_width=True)

with st.container(border=True):
    st.write("Financial Express News : ")
    for news in all_news:
        st.write("→ ", news)
