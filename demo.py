import urllib.request, json, csv
import datetime as datetime
import openpyxl

# Import the data from the CoinMarketCap public API
with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?convert=GBP") as url:
    data = json.loads(url.read().decode())

# Print a list of all coins and their GBP values
for x in range(0, len(data)):# Increment x from 0, to the length of data (our list)
    print("The current coin is: " + str(data[x]['id']) + " the current GBP rate is : " + str(data[x]['price_gbp']))

# Pull current date, and format it as year/month/day hour:minutes and save it as a variable
date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')

# Create a file to save the outputs
filename = 'output.csv'
f = open(filename,'a')

# Write the data to the csv file each time the programme runs
for x in range(0, len(data)):# Increment x from 0, to the length of data (our list)
    f.write("\n" + (data[x]['last_updated']) + "," + (data[x]['id']) + "," + (data[x]['price_gbp']) + "," + (data[x]['price_btc']) + "," + (date))
f.close()




    








