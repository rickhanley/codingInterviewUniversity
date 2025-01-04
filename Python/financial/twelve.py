import requests
import json

base_url = "https://api.twelvedata.com"

api_key = "48774f71e0854a3b87f406af7a0c28cb"

symbol = "GOOG"  # Replace with your stock symbol
interval = "1day"  # Supported intervals: 1min, 5min, 1h, 1day, etc.
outputsize = 180 

endpoint = f"{base_url}/time_series?symbol={symbol}&interval={interval}&outputsize={outputsize}&apikey={api_key}"

print(f"{base_url}{endpoint}")

try:
    # Full API URL
    # api_url = base_url + endpoint

    # Make the GET request
    response = requests.get(endpoint)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        with open("data.txt", "w") as file:
            json.dump(data, file, indent=4)  # Writes the formatted JSON to the file
        
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print("Response message:", response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    
    
