import requests
from bs4 import BeautifulSoup


def main():

    req = requests.get('https://dveribelorussii.com.ua/catalog/dveri/filter/vid_dveri-is-vhodnyie-dveri/sostav_polotna-is-metallicheskie/').content
    soup = BeautifulSoup(req, 'html.parser')


    div = soup.find_all('img', class_= 'img-responsive')

    for item in div: # после каждого find_all нужно делать итерацию(for)
        print(item.get('alt'))
    #link = soup.find('div', class_='paggination').find('a', class_='active').find_next().get('href')
    #print(div)

    for title in div:
        print(title.get('title'))

    if item != title:
        print('wrong')
    else: print(('success'))







# count=0
# for alt in img:
# alts = alt.get('alt')
# print(alts)
# if (count % 5 == 0):
# count+=1



if __name__ == '__main__':
    main()