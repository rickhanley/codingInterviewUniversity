import requests
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# API details
base_url = "https://api.twelvedata.com"
api_key = "48774f71e0854a3b87f406af7a0c28cb"
symbol = "GOOG"  # Stock symbol
interval = "1day"  # Interval (1 day)
outputsize = 180  # Number of days

# Construct the endpoint URL
endpoint = f"{base_url}/time_series?symbol={symbol}&interval={interval}&outputsize={outputsize}&apikey={api_key}"

# Make the GET request
response = requests.get(endpoint)

# Check for a successful response
if response.status_code == 200:
    data = response.json()

    # Extract the 'values' list (the actual stock data)
    values = data.get("values", [])

    # Initialize lists to store the data for plotting
    dates = []
    highs = []
    lows = []

    # Loop through the values and extract the necessary data
    for entry in values:
        dates.append(entry["datetime"])
        highs.append(float(entry["high"]))  # Convert to float for plotting
        lows.append(float(entry["low"]))    # Convert to float for plotting

    # Plotting
    plt.figure(figsize=(10, 5))  # Set the figure size

    # Plot the high and low prices
    plt.plot(dates, highs, label="High", color="green")
    plt.plot(dates, lows, label="Low", color="red")

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    # Set x-ticks to show every 7th date
    tick_interval = 7  # Show every 7th date
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=len(dates)//tick_interval))

    # Manually set the x-ticks to display every 7th date
    plt.xticks(dates[::tick_interval])

    # Add labels and title
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title(f"{symbol} Stock Price (High vs Low)")

    # Add a legend
    plt.legend()

    # Display the plot
    plt.tight_layout()
    plt.show()

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
