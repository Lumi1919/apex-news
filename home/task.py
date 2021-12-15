import requests

url = "https://api-nba-v1.p.rapidapi.com/seasons/"

headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "988e3fa109msha3b36c63d0d37ebp18c044jsn40db0e6e1028"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)