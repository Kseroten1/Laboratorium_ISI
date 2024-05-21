import requests
from bs4 import BeautifulSoup
import csv


class Home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name
        self.price = price
        self.price_for_m2 = price_for_m2


def scrape_homes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    homes = []

    offers = soup.find_all('div', class_='offer-item-details')
    for offer in offers:
        header = offer.find('span', class_='offer-item-title').text.strip()
        price = offer.find('li', class_='offer-item-price').text.strip()
        price_m2 = offer.find('li', class_='hidden-xs offer-item-price-per-m').text.strip()

        home = Home(header, price, price_m2)
        homes.append(home)

    return homes


def save_to_csv(homes):
    with open('home.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['header_name', 'price', 'price_for_m2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for home in homes:
            writer.writerow({'header_name': home.header_name, 'price': home.price, 'price_for_m2': home.price_for_m2})


if __name__ == "__main__":
    url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing"
    homes = scrape_homes(url)
    save_to_csv(homes)

