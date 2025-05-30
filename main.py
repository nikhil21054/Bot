from indicators import get_rsi_signal
import time

def main():
    while True:
        price_data = fetch_data()
        signal = get_rsi_signal(price_data)
        print(f"Signal: {signal}")
        time.sleep(60)

def fetch_data():
    # This should connect to Quotex's API or demo data
    return [mock_prices_here]

if __name__ == "__main__":
    main()
  
