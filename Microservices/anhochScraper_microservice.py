import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from IPython.display import HTML
requests.packages.urllib3.disable_warnings()
import warnings
import sys
warnings.filterwarnings('ignore')

def webParser(url):
    strana = requests.get(url)

    raw_html = strana.text
    soup = BeautifulSoup(raw_html,'html.parser')

    product_titles = soup.select('.product-name')
    product_price = soup.select('.nm')

    lista_produkti = [product.text for product in product_titles]
    products_prices_manufacturers = dict()
    products = []
    for i in range(len(lista_produkti)):
        if lista_produkti[i] not in products_prices_manufacturers:
            products.append(lista_produkti[i])
            products_manufacturer = lista_produkti[i].split()
            products_manufacturer = products_manufacturer[0]
            products_prices_manufacturers[lista_produkti[i]] = [product_price[i].text,products_manufacturer]

    for key, value in products_prices_manufacturers.items():
        print(key, ' : ', value)
        sys.stdout.flush()

if __name__ == '__main__':

    urls = ["https://www.anhoch.com/category/374/grafichki-kartichki#page/1/",
          "https://www.anhoch.com/category/374/grafichki-kartichki/page/2",
          "https://www.anhoch.com/category/374/grafichki-kartichki/page/3",
          "https://www.anhoch.com/category/374/grafichki-kartichki/page/4",
          "https://www.anhoch.com/category/374/grafichki-kartichki/page/5",
          "https://www.anhoch.com/category/374/grafichki-kartichki/page/6",
          "https://www.anhoch.com/category/374/grafichki-kartichki/page/7"]

    for url in urls:
        webParser(url)
        sys.stdout.flush()

