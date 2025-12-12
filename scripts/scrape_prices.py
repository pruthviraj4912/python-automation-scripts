import requests
from bs4 import BeautifulSoup

url = "https://example.com/products"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = []
for item in soup.select(".product-card"):
    name = item.select_one(".title").get_text(strip=True)
    price = item.select_one(".price").get_text(strip=True)
    products.append({"name": name, "price": price})

print(products)
