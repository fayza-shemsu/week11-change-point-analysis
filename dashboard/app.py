import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from src.data_loader import load_brent_data

st.title("Brent Oil Price Change Point Analysis")

df = load_brent_data("data/raw/brentoilprices.csv")

st.subheader("Brent Oil Prices")
fig, ax = plt.subplots()
ax.plot(df.index, df["Price"])
st.pyplot(fig)

st.subheader("Log Returns")
df["log_return"] = np.log(df["Price"]).diff()
fig, ax = plt.subplots()
ax.plot(df.index, df["log_return"])
st.pyplot(fig)

st.markdown("""
### Insights
- Oil prices show long-term trends and volatility clustering
- Log returns stabilize the series
- Structural breaks suggest regime changes
""")
