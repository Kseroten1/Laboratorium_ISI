import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.wp.pl")
print(response)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
links = soup.find_all("a") # Find all elements with the tag <a>
for link in links:
  print("Link:", link.get("href"), "Text:", link.string)
