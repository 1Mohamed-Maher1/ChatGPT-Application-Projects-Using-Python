import requests
from bs4 import BeautifulSoup

response = requests.get("http://books.toscrape.com/")

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    price = book.find("p", class_="price_color").text
    print("Book titled: " + title + " has a rating of: " + rating + "stars" + " price= " + price)

print(books[0])