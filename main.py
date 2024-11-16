import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,ripple,litecoin,cardano,dogecoin,solana,polkadot,binancecoin,uniswap,terra,chainlink,shiba-inu,algorand,tron,monero,vechain,cosmos,neo,steem,tezos,theta,yearn-finance,hedera,elrond,aptos,flow,bittorrent,zcash,kucoin-shares,ftx-token,hedera,terra-luna-2.0,compound,dash,bitcoin-cash,eos,bat,link,maker,sushi,dai,compound,decubate,lido-staked-ether,polygon,polkadot,bnb,quantum-computing-network,dogelon-mars,harmony,safemoon,litecoin,lisk',
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data, status code: {response.status_code}")
        return None

data = fetch_crypto_data()

if data:
    try:
        if isinstance(data, list):
            df = pd.DataFrame(data)
            print(df.head())
            df = df[['name', 'current_price', 'market_cap', 'total_supply', 'price_change_percentage_24h']]
            df = df.sort_values(by='market_cap', ascending=False)

            fig, ax = plt.subplots(figsize=(12, 8))
            ax.barh(df['name'], df['market_cap'], color='skyblue', label='Market Cap')
            ax.set_xlabel('Market Cap (in USD)')
            ax.set_title('Cryptocurrency Market Capitalization')
            ax.grid(True)
            plt.tight_layout()
            plt.show()

            fig, ax2 = plt.subplots(figsize=(12, 8))
            ax2.barh(df['name'], df['price_change_percentage_24h'], color='lightcoral', label='24h Price Change (%)')
            ax2.set_xlabel('Price Change (%)')
            ax2.set_title('Cryptocurrency 24-hour Price Change')
            ax2.grid(True)
            plt.tight_layout()
            plt.show()

            df.to_csv('crypto_market_data.csv', index=False)
            print("Data saved to 'crypto_market_data.csv'.")
        else:
            print("Error: API returned data in unexpected format.")
    except Exception as e:
        print(f"An error occurred while processing the data: {e}")
else:
    print("No data to display.")
