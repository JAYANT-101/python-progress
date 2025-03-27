from http.client import responses
from bs4 import BeautifulSoup
import requests
# response=requests.get("https://www.youtube.com")
# print(response.text)
# url = "https://jsonplaceholder.typicode.com/posts"
#
# data = {
#     "title": 'Jayant',
#     "body": 'bro',
#     "userId": 11,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)
#
# print(response.text)
url="https://www.codewithharry.com/blogpaost?django-chetsheet/"
r=requests.get(url)
print(r.text)
soup=BeautifulSoup(r.text,'html.parser')
for heading in soup.find_all("h2"):
    print(heading.text)