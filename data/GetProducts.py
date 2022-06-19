from bs4 import BeautifulSoup
import requests

from models.Product import make_product


def get_products(product_name):
    product_index = product_name.strip().replace(' ', '-')

    url = f'https://games.mercadolivre.com.br/consoles/{product_index}_NoIndex_True'
    layout_class = 'ui-search-layout__item'
    img_class = 'ui-search-result-image__element' 
    price_class = 'price-tag-fraction'

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    products = soup.findAll('li', class_ = layout_class)

    formattedProducts = []

    for product in products:
        image = product.find('img', class_ = img_class)['data-src']
        price = product.find('span', class_ = price_class).text.replace(' ', '')
        title = product.find('h2').text

        print(f'''
            Product name: {title}
            Product price: {price}
            Product image url: {image}
        ''')

        formattedProducts.append(make_product(title, image, price))

    return formattedProducts