import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def run():
    for i in range(1, 6): 
        response = requests.get('http://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')
        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print('Descargando la imagen {}'.format(image_name))
        urlretrieve(f'https:{image_url}', image_name)


if _name_ == '_main_':
    run()