import requests
from bs4 import BeautifulSoup

url = "https://blog.python.org/blog/"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

# Get all post titles
titles = soup.find_all("h3")

for title in titles:
    print(title.get_text(strip=True))
