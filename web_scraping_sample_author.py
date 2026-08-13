import requests
from bs4 import BeautifulSoup

url = "https://blog.python.org/blog/"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

# Get all post titles
titles = soup.find_all("h3")

for title in titles:
    # Get the post container
    post = title.find_parent()

    # Find the author link inside the same post
    author = post.find_next("a")

    if author:
        print(author.get_text(strip=True))
