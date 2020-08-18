import requests
from bs4 import BeautifulSoup
import urllib.request


def run():
    ultima_imagen = int(input("¿Cuantas imagenes quieres descargar?: "))
    for i in range(1,ultima_imagen+1): #!Descargará desde la imagen 1 hasta la que digamos
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')
        image_url = image_container.find('img')['src']
        imagen_name = image_url.split('/')[-1]
        print('Descargando la imagen {}'.format(imagen_name)) #!Esto es sólo para que veamos que sí está funcionando
        urllib.request.urlretrieve('https:{}'.format(image_url), imagen_name)


if __name__ == "__main__":
    run()