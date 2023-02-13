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

    product_titles = soup.select('.name')
    product_prices = soup.select('.price-old-new')

    products_prices_manufacturers = dict()
    for i in range(len(product_titles)):
        products_split = product_titles[i]
        products_split = str(products_split).split()
        #print(products_split)
        productStr = ""
        product_titles1 = []
        for j in range(4,len(products_split)-1):
            productStr = productStr + " "+ products_split[j]

        productStr = productStr[:-4]
        product_titles1.append(productStr)
        product_price = product_prices[i].text
        product_priceSplit = product_price.split()
        product_price = product_priceSplit[0]
        product_manufacturer = productStr.split()
        product_manufacturer = product_manufacturer[0]
        products_prices_manufacturers[productStr] = [product_price,product_manufacturer]

    for key, value in products_prices_manufacturers.items():
        print(key, ' : ', value)
        sys.stdout.flush()


if __name__ == '__main__':

    urls = ["https://setec.mk/index.php?route=product/category&path=10019_10020_10025",
            "https://setec.mk/index.php?route=product/category&path=10019_10020_10025&page=2",
            "https://setec.mk/index.php?route=product/category&path=10019_10020_10025&page=3"]

    for url in urls:
        webParser(url)
        sys.stdout.flush()

