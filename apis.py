import requests

url = "https://api.adviceslip.com/advice"

response = requests.request("GET", url)

print(response.text)