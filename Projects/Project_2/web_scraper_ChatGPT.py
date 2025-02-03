import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "http://books.toscrape.com/"

# Send an HTTP request to the page
response = requests.get(url)
# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all book containers
books = soup.find_all("article", class_="product_pod")

# Loop through each book and extract title, rating, and price
for book in books:
    # Extract title
    title = book.h3.a["title"]

    # Extract price
    price = book.find("p", class_="price_color").text

    # Extract rating (e.g., "star-rating Three" -> "Three")
    rating = book.find("p", class_="star-rating")["class"][1]

    # Print extracted information
    print(f"Title: {title}\nRating: {rating}\nPrice: {price}\n")
