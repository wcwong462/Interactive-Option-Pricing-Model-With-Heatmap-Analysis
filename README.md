# Black-Scholes Option Pricing Model

A comprehensive web application built with Streamlit for calculating option prices and analyzing option sensitivity using the Black-Scholes model.

## Features

- **Interactive Option Pricing**: Calculate call and put option prices using the Black-Scholes formula
- **Greeks Calculation**: Compute all major option Greeks (Delta, Gamma, Vega, Theta, Rho)
- **Visual Heatmaps**: Interactive heatmaps showing option price sensitivity to spot price and volatility
- **Real-time Updates**: All calculations update automatically when parameters change
- **Professional UI**: Clean, intuitive interface with organized parameter inputs

## Project Structure

```
Black-Scholes-Equation/
├── app.py           # Main Streamlit application
├── model.py         # Black-Scholes calculations and Greeks
├── heatMap.py       # Heatmap visualization functions
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Project Idea

The Project references a YouTube video listed below:
https://youtu.be/lY-NP4X455U?si=aosBN1smdiqcB1f4

More functionality & Styling will be updated

## Mathematical Foundation

The Black-Scholes model calculates option prices using:

**Call Option Price:**
```
C = S₀ × N(d₁) - K × e^(-rT) × N(d₂)
```

**Put Option Price:**
```
P = K × e^(-rT) × N(-d₂) - S₀ × N(-d₁)
```

Where:
- `d₁ = [ln(S₀/K) + (r + σ²/2)T] / (σ√T)`
- `d₂ = d₁ - σ√T`
- `S₀` = Current stock price
- `K` = Strike price
- `T` = Time to expiration
- `r` = Risk-free interest rate
- `σ` = Volatility
- `N(x)` = Cumulative standard normal distribution

## Greeks Implemented

- **Delta (Δ)**: Price sensitivity to underlying asset price changes
- **Gamma (Γ)**: Rate of change of delta
- **Vega (ν)**: Sensitivity to volatility changes
- **Theta (Θ)**: Time decay of the option
- **Rho (ρ)**: Sensitivity to interest rate changes

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wcwong462/Interactive-Option-Pricing-Model-With-Heatmap-Analysis.git
   cd Black-Scholes-Equation
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to `http://localhost:8501`

3. **Adjust parameters** in the sidebar:
   - Current Stock Price (S)
   - Strike Price (K)
   - Time to Expiration (T)
   - Risk-free Interest Rate (r)
   - Volatility (σ)

4. **View results:**
   - Option prices displayed in real-time
   - Interactive heatmaps showing price sensitivity
   - Complete Greeks analysis

## Input Parameters

| Parameter | Description | Example Value |
|-----------|-------------|---------------|
| **S** | Current stock price | $100.00 |
| **K** | Strike price | $100.00 |
| **T** | Time to expiration (years) | 1.0 |
| **r** | Risk-free interest rate | 0.05 (5%) |
| **σ** | Volatility | 0.20 (20%) |

## Heatmap Analysis

The application generates interactive heatmaps showing:
- **Call Option Prices** across different spot prices and volatilities
- **Put Option Prices** with the same parameter ranges
- **Color-coded visualization** for easy interpretation
- **Customizable ranges** for spot price and volatility

## Technical Details

- **Backend**: Python 3.8+
- **Frontend**: Streamlit
- **Visualization**: Matplotlib, Seaborn
- **Mathematical Computing**: NumPy, SciPy
- **Statistics**: scipy.stats.norm for cumulative distribution functions

## File Descriptions

### `app.py`
Main Streamlit application containing:
- User interface layout
- Parameter input widgets
- Real-time calculation display
- Heatmap integration

### `model.py`
Core mathematical functions:
- `calculate_option_prices()`: Black-Scholes option pricing
- `calculate_greeks()`: Option sensitivity calculations

### `heatMap.py`
Visualization functions:
- `call_option_heatmap()`: Call option price heatmaps
- `put_option_heatmap()`: Put option price heatmaps

### `analysis.py`
Additional analysis tools for:
- Batch calculations
- Sensitivity analysis
- Custom testing scenarios

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Samuel Wong**

## Acknowledgments

- Black-Scholes model by Fischer Black, Myron Scholes, and Robert Merton
- Streamlit for the excellent web framework
- SciPy for statistical distributions

---
