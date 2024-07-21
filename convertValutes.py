# IMPORTS -----------
import os
from dotenv import load_dotenv
import requests
from datetime import datetime
# ----------

# get currencies from file instead of API to not spend free requests, file from official documentation
f = open('currencies.txt')
currencies = {}
names = []
codes = []
for i in range(161):
    curr, name, country = f.readline().strip().split("	")
    currencies[name] = curr
    names += [f"{name} ({curr})"]
    codes += [curr]

load_dotenv()
def convert(base, target, amount):
    if base not in codes or target not in codes: return f"Wrong currency selected: {base}, {target}, {amount}"

    api_key = os.getenv("API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base}/{target}"
    # url must contains: api key, two valutes: first - from which we convert, second - to which we convert

    response = requests.get(url)
    if response.status_code == 200: # if request is ok
        data = response.json()

        unixUpdateTime = data["time_last_update_unix"] # get time in unix (time since 1 jan 1970)
        conversion_rate = data["conversion_rate"] # valutes modifier

        updateTime = datetime.fromtimestamp(unixUpdateTime) # convert unix time to normal date
        result = amount * conversion_rate # counting amount

        return (f"{amount} {base}: {result} {target}\n"
                f"Last time update: {updateTime}\n"
                f"Current exchange rate: 1 {base} = {conversion_rate} {target}")
    else: # if request is bad
        return "Error while converting"