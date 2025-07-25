import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from model import calculate_option_prices, calculate_greeks
from heatMap import call_option_heatmap, put_option_heatmap

st.set_page_config(page_title="Black-Scholes Option Pricing", layout="wide")
st.write("# Black-Scholes Option Pricing Model")
col1, col2 = st.columns([1,2])

st.sidebar.title("Made by Samuel Wong")
st.sidebar.header("Input Parameters")
S = st.sidebar.number_input("Current Stock Price (S)", min_value=0.0, value=100.0)
K = st.sidebar.number_input("Strike Price (K)", min_value=0.0, value=100.0)
T = st.sidebar.number_input("Time to Expiration (T in years)", min_value=0.0, value=1.0)
r = st.sidebar.number_input("Risk-Free Interest Rate (r)", min_value=0.0, value=0.05)
sigma = st.sidebar.number_input("Volatility (σ)", min_value=0.0, value=0.2)
st.sidebar.divider()
S_min = st.sidebar.number_input("Minimum Spot Price", min_value=0.0, value=50.0)
S_max = st.sidebar.number_input("Maximum Spot Price", min_value=0.0, value=150.0)
Volatility_min = st.sidebar.slider("Minimum Volatility", min_value=0.0, value=0.1)
Volatility_max = st.sidebar.slider("Maximum Volatility", min_value=0.0, value=1.0)


delta, gamma, vega, theta, rho = calculate_greeks(S, K, T, r, sigma)
call_price, put_price = calculate_option_prices(S, K, T, r, sigma)


st.write("### Option Prices:")

with col1:
    st.write(f"Call Price: {call_price}")
    call_fig = call_option_heatmap(S_min, S_max, Volatility_min, Volatility_max, r, T, K)
    st.pyplot(call_fig)
    plt.close(call_fig)

with col2:
    st.write(f"Put Price: {put_price}")
    put_fig = put_option_heatmap(S_min, S_max, Volatility_min, Volatility_max, r, T, K)
    st.pyplot(put_fig)
    plt.close(put_fig)



st.write("### Greeks:")
st.write(f"Delta: {delta}")
st.write(f"Gamma: {gamma}")
st.write(f"Vega: {vega}")
st.write(f"Theta: {theta}")
st.write(f"Rho: {rho}")
    

