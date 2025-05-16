import requests

api_key = "7120175e997a4aae8edc62c5167858bf"

url = "https://newsapi.org/v2/everything?q=tesla&from=2025-04-16&" \
      "sortBy=publishedAt&apiKey=" \
      "7120175e997a4aae8edc62c5167858bf"

request = requests.get(url)
content=request.json()
for article in content["articles"]:
    print(article["title"])
