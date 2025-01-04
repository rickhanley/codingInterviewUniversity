import requests

# Twelve Data API Key (replace with your actual key)
api_key = "48774f71e0854a3b87f406af7a0c28cb"

# Base URL for Twelve Data API
base_url = "https://api.twelvedata.com"

# Parameters for the API call
symbol = "AAPL"  # Replace with your stock symbol
interval = "1day"  # Supported intervals: 1min, 5min, 1h, 1day, etc.
outputsize = 30  # Number of data points (30 days of data in this case)

# Construct the full API endpoint
endpoint = f"{base_url}/time_series?symbol={symbol}&interval={interval}&outputsize={outputsize}&apikey={api_key}"

try:
    # Make the API request
    response = requests.get(endpoint)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if "values" in data:
            # Print the historical data
            for entry in data["values"]:
                print(f"Date: {entry['datetime']}, Close Price: {entry['close']}")
        else:
            print("Error in response:", data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print("Response message:", response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
