# pip install requests
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import uniform


def access_website(url: str) -> list:
    '''
    RETURN: content <html></html> of website
    '''
    API_KEY = "ceff3229258c2096cfb481055b4f0d80b86887cd"
    PARAMS = {
        "url": url,
        "apikey": API_KEY,
    }

    print(f"Accessing {url}...")
    response = requests.get("https://api.zenrows.com/v1/", params=PARAMS)
    
    if response.status_code == 200:
        print(f"\033[92mSuccessful access\033[00m {url}")
    
    else:
        print(f"\033[31mAccess deny\033[00m {url}")
        return None
    
    response.close()

    wait_ = uniform(3,5)
    print(f"Waiting {wait_}s...")
    sleep(wait_)
    return response.content


def get_product_links_from(url: str):
    '''
    url: "https://www.bhphotovideo.com/c/buy/laptops/ci/18818/pn/2"
    RETURN: All products of the subpage url
    [
        https://www.bhphotovideo.com/c/product/1761584-REG/hp_804m4ua_aba_zbook_studio_g9_mobile.html,
        https://www.bhphotovideo.com/c/product/1764370-REG/hp_822p5ut_aba_15_6_probook_450_g10.html,
        ...
    ]
    '''
    raw_content = access_website(url=url)
    if raw_content is None:
        return None
    
    soup = BeautifulSoup(raw_content, "html.parser")

    product_links = list()

    try:
        a_tags = soup.find_all("a", class_="title_UCJ1nUFwhh")
        for a_tag in a_tags:
            product_link = "https://www.bhphotovideo.com" + a_tag.get("href")
            product_links.append(product_link)
        
    except:
        print("Not found!")
    
    return product_links


def get_subpages_from(base_url: str, numbers: list, page_num="/pn/_") -> list:
    '''
    base_url: "https://www.bhphotovideo.com/c/buy/laptops/ci/18818"
    # RETURN: List of subpage to get product links
    [
        "https://www.bhphotovideo.com/c/buy/laptops/ci/18818/pn/1",
        "https://www.bhphotovideo.com/c/buy/laptops/ci/18818/pn/2",
        "https://www.bhphotovideo.com/c/buy/laptops/ci/18818/pn/3",
        ...
    ]
    '''

    subpages = [None]
    for pgn in numbers:
        subpage = base_url + page_num.replace("_", str(pgn))
        subpages.append(subpage)

    return subpages


def write_txt(filepath: str, product_links: list):
    '''
    filepath: in the same folder of the current file
    links: list of product_links
    links=[
        https://www.bhphotovideo.com/c/product/1793833-REG/apple_mbp14m345sl_14_macbook_pro_m3.html,
        https://www.bhphotovideo.com/c/product/1793822-REG/apple_mbp14m340sb_14_macbook_pro_m3.html,
        ...
    ]
    write each product in a line of file .txt
    '''
    try:
        with open(filepath, 'a', encoding='utf-8') as f:
            for link in product_links:
                f.write(f"{link}\n")
        
        print(f"Successful saving to {filepath}")
    
    except:
        print(f"Error with {filepath}")


if __name__ == "__main__":
    BASE_URL = "https://www.bhphotovideo.com/c/buy/laptops/ci/18818"
    FILEPATH = "bhphotovideo_items.txt"
    
    # SCRAPING FROM PAGE 1 -> PAGE 51
    subpages = get_subpages_from(base_url=BASE_URL, numbers=range(1, 52), page_num="/pn/_")
    stack = subpages.copy()

    while stack.__len__() != 1:
        subpage = stack.pop(0)
        links = get_product_links_from(subpage)

        if links == None:
            stack.append(subpage)

        else:
            write_txt(filepath=FILEPATH, product_links=links)
