import requests


open_page = requests.get('https://dveribelorussii.com.ua/robots.txt') # open page

writing_file = open("robots.txt") # open empty file

writing_file = open
read = open_page.text # writing data to read from page

#out_file = 'robots.txt' #create out_file

#open(out_file, 'w') #open out_File to write

#open(out_file, 'a').write(read)

file_origin = open("123.txt")# origin file open

data = file_origin.read() #writing data in data from file_origin

#out_reading = open(out_file, 'r').read()


print(data)
#if data != out_reading:
    #print('wrong')



