from bhphotovideo import *

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
    raw_content = access_website(url=specs_url)
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
