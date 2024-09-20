import requests
url="https://v6.exchangerate-api.com/v6/9d6dcf8adcbb87d02528ea74/latest/USD"
response=requests.get(url)
if response.status_code== 200:
    currency_converter=response.json()
    amount_in_eur=float(input(" enter amount_in_eur ") )
    usd_to_eur = currency_converter['conversion_rates']['EUR']
    amount_in_usd = amount_in_eur / usd_to_eur

    print(f"{amount_in_eur} EUR is equal to {amount_in_usd:.2f} USD")

