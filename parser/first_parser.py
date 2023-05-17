import requests
from bs4 import BeautifulSoup
import json


url = 'http://health-diet.ru'

with open("export.json") as file:
    items = json.load(file)

items_attr_= {}

for item_text,item_href in items.items():
    print(item_text)
    href = f'{url}{item_href}'

    with open(f"pages/{item_text}.html") as file:
        page = file.read()

    parser = BeautifulSoup(page, "html.parser")

    item_attributes = parser.find(class_='uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed').find('tbody').find_all('tr')


    for item_attr in item_attributes:
        
        product_ids = item_attr.find_all("td")
        
        product = product_ids[0].find("a").text
        calories = product_ids[1].text
        belki = product_ids[2].text
        fats = product_ids[3].text
        uglevodi = product_ids[4].text

        items_attr_[product] = calories




with open(f"items/products_attr.json", 'w') as file:
    json.dump(items_attr_,file,indent=4,ensure_ascii=False)




