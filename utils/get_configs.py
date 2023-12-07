import os
import sys

import requests
from bs4 import BeautifulSoup
from random import uniform
from time import sleep

from common import access_website_js_render

def get_config_details_from(url: str) -> dict:
    '''
    url: https://www.bhphotovideo.com/c/product/1710341-REG/apple_mbam2mn_15_13_6_macbook_air_m2.html
    specs_url: url + "/specs
    RETURN: Configuration detail of "laptop_link"
        {
            "Operating System": "macOS",
            "Processor": "Apple M2",
            "GPU": "Apple (10-Core)",
            ...
        }
    '''
    specs_url = url + "/specs"
    raw_content = access_website_js_render(url=specs_url)
    soup = BeautifulSoup(raw_content, "html.parser")

    config_detail = dict()
    try:
        # Extract name : "HP 16" ZBook Studio G9 Mobile Workstation Wolf Pro Security Edition"
        product_name = ""
        product_name = soup.find("h1", class_="text_TAw0W35QK_").text
        if product_name:
            print("Name :",product_name)
        
        # Extract price: "$1,599.00"
        product_price = ""
        product_price = soup.find("div", class_="price__9gLfjPSjp").text
        if product_price:
            print("Price:",product_price)
        
        # Map product_name to dictionary
        config_detail["Name"] = product_name

        # pair_KqJ3Q3GPKv keySpec_KqJ3Q3GPKv
        config_tags = soup.find_all("tr", class_="pair_KqJ3Q3GPKv")

        for config_tag in config_tags:
            label, value = "", ""
            label = config_tag.find("td", class_="label_KqJ3Q3GPKv").text
            value_tag = config_tag.find("td", class_="value_KqJ3Q3GPKv")
            value = value_tag.find("span").text

            if label not in config_detail.keys():
                config_detail[label] = value
        
        config_detail["Price"] = product_price

        return config_detail

    except:
        print("Not found configuration!")

    return config_detail


if __name__ == '__main__':
    BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    RAW_DATA_PATH = os.path.join(BASE_PATH,"data", "raw")

    FILEPATH = "bhphotovideo_items.txt"
    SCRAPING_DATA_PATH = os.path.join(RAW_DATA_PATH, FILEPATH)
    
    product_links = []
    with open(SCRAPING_DATA_PATH, "r") as f:
        for line in f.readlines():
            product_links.append(line[:-1])
    
    # product_links.__len__() = 1422. So I divide to 9 times for scraping
    # 1 : [0:150]    # 5 : [601:750]
    # 2 : [151:300]  # 6 : [751-900]
    # 3 : [301:450]  # 7 : [901-1050]
    # 4 : [451:600]  # 8 : [1051-1200]
    # 9 : [1201-1421]

    product_links = product_links[0:2]
    stack = product_links.copy()

    all_product_configs = []
    while stack.__len__() != 0:
        product_link = stack.pop(0)

        config_detail = get_config_details_from(product_link)

        if config_detail is None:
            stack.append(product_link)
        
        else:
            all_product_configs.append(config_detail)

    print(all_product_configs)