# Cryptocurrency Market Analysis

This project explores the market capitalization and price data of over 50 cryptocurrencies using the CoinGecko API. The data is retrieved, processed, and visualized using Python libraries such as `requests`, `pandas`, and `matplotlib`.

## Installation

To run this project on your local machine, follow the steps below:

### Prerequisites:
- Python 3.x
- pip (Python's package installer)

### Steps to Install:
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/sarthidarji128/cryptocurrency-market-analysis.git
   ```

2. Navigate to the project directory:
   ```bash
   cd cryptocurrency-market-analysis
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Requirements:
Create a `requirements.txt` file that contains the following libraries:
```text
requests
pandas
matplotlib
```

## How to Run

Once the dependencies are installed, you can run the script to fetch cryptocurrency market data and visualize it.

1. Run the Python script:
   ```bash
   python main.py
   ```

2. The script will fetch data from the CoinGecko API, process it, and generate two visualizations:
   - A bar chart displaying the market capitalization of the cryptocurrencies.
   - A bar chart displaying the 24-hour price change percentage.

3. The data will also be saved in a CSV file named `crypto_market_data.csv` in the same directory.

here is the output

<img width="1199" alt="Screenshot 2024-11-16 at 4 33 06 PM" src="https://github.com/user-attachments/assets/e65c6959-22ec-4b21-9d98-e71df2e4e76d">

<img width="1200" alt="Screenshot 2024-11-16 at 4 33 22 PM" src="https://github.com/user-attachments/assets/28cd78b1-aa31-46c7-95cb-bd081f40dde8">

