import requests

open_page = requests.get('https://dveribelorussii.com.ua/robots.txt')

page_content = open_page.content

new_file = open('robots.txt', 'w')

new_file.write(str(page_content))

new_file.close()

new_file = open('robots.txt', 'r')

data1 = new_file.read()

#print(data1)

file_origin = open("123.txt")# origin file open

data = file_origin.read() #writing data in data from file_origin

if data == data1:
    print('ok')
else:
    print('wrong')





