import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# 📌 시가총액 상위 10개 기업의 티커 목록
top_10_tickers = [
    'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA',
    'BRK-B', 'NVDA', 'META', 'V', 'JNJ'
]

# 📅 데이터 다운로드
data = {}
for ticker in top_10_tickers:
    stock = yf.Ticker(ticker)
    data[ticker] = stock.history(period="1y")['Close']

# 📈 Plotly를 사용한 시각화
fig = go.Figure()

for ticker, prices in data.items():
    fig.add_trace(go.Scatter(
        x=prices.index,
        y=prices,
        mode='lines',
        name=ticker,
        line=dict(width=2)
    ))

fig.update_layout(
    title="Global Top 10 Market Cap Stocks - Last 1 Year",
    xaxis_title="Date",
    yaxis_title="Closing Price (USD)",
    template="plotly_dark",
    hovermode="x unified"
)

# 📺 Streamlit에 시각화 표시
st.plotly_chart(fig)
