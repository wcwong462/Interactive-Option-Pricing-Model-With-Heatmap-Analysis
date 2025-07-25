import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from model import calculate_option_prices, calculate_greeks
from heatMap import option_heatmap

st.set_page_config(page_title="Option Pricing & Heatmap Analysis", layout="wide")
st.write("# Option Pricing & Heatmap Analysis")

with st.sidebar:

    st.sidebar.title("Made by Samuel Wong")
    st.sidebar.header("Input Parameters")
    S = st.sidebar.number_input("Spot Price (S)", min_value=0.0, value=100.0)
    K = st.sidebar.number_input("Strike Price (K)", min_value=0.0, value=100.0)
    T = st.sidebar.number_input("Time to Expiration (T in years)", min_value=0.0, value=1.0)
    r = st.sidebar.number_input("Risk-Free Interest Rate (r)", min_value=0.0, value=0.05)
    sigma = st.sidebar.number_input("Volatility (σ)", min_value=0.0, value=0.2)

    call_price, put_price = calculate_option_prices(S, K, T, r, sigma)

    st.sidebar.divider()

    st.sidebar.header("Heatmap Inputs")
    S_min = st.sidebar.number_input("Minimum Spot Price", min_value=0.0, value=50.0)
    S_max = st.sidebar.number_input("Maximum Spot Price", min_value=0.0, value=150.0)
    Volatility_min = st.sidebar.slider("Minimum Volatility", min_value=0.0, value=0.1)
    Volatility_max = st.sidebar.slider("Maximum Volatility", min_value=0.0, value=1.0)

    delta, gamma, vega, theta, rho = calculate_greeks(S, K, T, r, sigma)


option_body = st.container()
with option_body:
    st.write("### Black-Scholes Model Option Pricings:")

    call_col, put_col = st.columns(2)

    with call_col:
        st.write(f"#### Call Price: ${call_price:.2f}")
        call_fig = option_heatmap(S_min, S_max, Volatility_min, Volatility_max, r, T, K)[0]
        st.pyplot(call_fig)
        plt.close(call_fig)

    with put_col:
        st.write(f"####     Put Price: ${put_price:.2f}")
        put_fig = option_heatmap(S_min, S_max, Volatility_min, Volatility_max, r, T, K)[1]
        st.pyplot(put_fig)
        plt.close(put_fig)

greeks_body = st.container()

with greeks_body:

    st.write("### Greeks:")
    st.write(f"Delta: {delta}")
    st.write(f"Gamma: {gamma}")
    st.write(f"Vega: {vega}")
    st.write(f"Theta: {theta}")
    st.write(f"Rho: {rho}")
