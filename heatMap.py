import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from model import calculate_option_prices, calculate_greeks

def call_option_heatmap(S_min, S_max, sigma_min, sigma_max, r, T, K):
    S_values = np.linspace(S_min, S_max, 10)
    sigma_values = np.linspace(sigma_min, sigma_max, 10)
    S_grid, sigma_grid = np.meshgrid(S_values, sigma_values)
    
    call_price = calculate_option_prices(S_grid, K, T, r, sigma_grid)[0]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(call_price, cmap='viridis', annot=True, fmt=".2f", ax=ax,
                xticklabels=np.round(S_values, 1),
                yticklabels=np.round(sigma_values, 3))
    ax.set_title('Call Option Price Heatmap')
    ax.set_xlabel('Spot Price (S)')
    ax.set_ylabel('Volatility (σ)')
    
    return fig

def put_option_heatmap(S_min, S_max, sigma_min, sigma_max, r, T, K):
    S_values = np.linspace(S_min, S_max, 10)
    sigma_values = np.linspace(sigma_min, sigma_max, 10)
    S_grid, sigma_grid = np.meshgrid(S_values, sigma_values)
    
    put_price = calculate_option_prices(S_grid, K, T, r, sigma_grid)[1]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(put_price, cmap='viridis', annot=True, fmt=".2f", ax=ax,
                xticklabels=np.round(S_values, 1),
                yticklabels=np.round(sigma_values, 3))
    ax.set_title('Put Option Price Heatmap')
    ax.set_xlabel('Spot Price (S)')
    ax.set_ylabel('Volatility (σ)')
    
    return fig
