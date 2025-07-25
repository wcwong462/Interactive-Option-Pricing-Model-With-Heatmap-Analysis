import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from model import calculate_option_prices, calculate_greeks

def option_heatmap(S_min, S_max, sigma_min, sigma_max, r, T, K):
    S_values = np.linspace(S_min, S_max, 10)
    sigma_values = np.linspace(sigma_min, sigma_max, 10)
    S_grid, sigma_grid = np.meshgrid(S_values, sigma_values)
    
    call_price, put_price = calculate_option_prices(S_grid, K, T, r, sigma_grid)

    # Create figures for call and put
    call_fig, ax1 = plt.subplots(figsize=(10, 8))
    sns.heatmap(call_price, cmap='viridis', annot=True, fmt=".2f", ax=ax1,
                xticklabels=np.round(S_values, 2),
                yticklabels=np.round(sigma_values, 2))
    ax1.set_title('Call Option Price Heatmap')
    ax1.set_xlabel('Spot Price (S)')
    ax1.set_ylabel('Volatility (σ)')

    put_fig, ax2 = plt.subplots(figsize=(10, 8))
    sns.heatmap(put_price, cmap='viridis', annot=True, fmt=".2f", ax=ax2,
                xticklabels=np.round(S_values, 2),
                yticklabels=np.round(sigma_values, 2))
    ax2.set_title('Put Option Price Heatmap')
    ax2.set_xlabel('Spot Price (S)')
    ax2.set_ylabel('Volatility (σ)')

    return call_fig, put_fig


