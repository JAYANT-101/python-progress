import requests
import json
qr=input("What type of news you want\n")
url= f"https://newsapi.org/v2/everything?q={qr}&from=2025-02-27&sortBy=publishedAt&apiKey=acb50ad7580943ae80106f971f81862e"
e=requests.get(url)
news =json.loads(e.text)
# print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------")