import requests

amount = float(input("Enter the amount: "))
from_currency = input("From Currency (USD, INR, BDT, GBP): ").upper()
to_currency = input("To Currency (USD, INR, BDT, GBP): ").upper()

url = f"https://open.er-api.com/v6/latest/{from_currency}"

response = requests.get(url).json()

if response["result"] == "success":
    rate = response["rates"][to_currency]
    converted = amount * rate
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("❌ Currency rates not available right now. Try again later.")





"""
Enter the amount: 100
From Currency (USD, INR, BDT, GBP): USD
To Currency (USD, INR, BDT, GBP): INR
100.0 USD = 8990.74 INR

"""
