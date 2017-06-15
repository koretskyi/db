import requests
from bs4 import BeautifulSoup


def main():

    req = requests.get('https://dveribelorussii.com.ua/catalog/dveri/filter/vid_dveri-is-vhodnyie-dveri/sostav_polotna-is-metallicheskie/').content
    soup = BeautifulSoup(req, 'html.parser')

    title = soup.select("head title")
    print(title)# как вывести сообщение, если тайтл отсутствует


if __name__ == '__main__':
    main()