import requests

# Base URL for the Finnhub API
base_url = "https://finnhub.io/api/v1"

# Your API key (replace with your actual key)
api_key = "ctr9r09r01qhb16md4o0ctr9r09r01qhb16md4og"

# Example endpoint to get stock quotes
symbol = "GOOG"  # Replace with the stock ticker you're interested in
endpoint = f"/quote?symbol={symbol}&token={api_key}"

try:
    # Full API URL
    api_url = base_url + endpoint

    # Make the GET request
    response = requests.get(api_url)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        print("Stock Quote Data:", data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print("Response message:", response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
