import requests
from box import Box
response = requests.get("https://api.exchangeratesapi.io/latest?symbols=USD")
b = Box(response.json())
print("1 euro is", b.rates.USD, "dollars.")