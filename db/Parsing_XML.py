file = 'sitemap.txt'  # name of input file with data

out_file = 'url_file.txt'  # name of out file with url

data = open(file, 'r').read()

list_url = data.split('<loc>')

out_url_list = []

open(out_file, 'w')  # clean out file before writing

for elem in list_url:

    if '</loc>' in elem:

        url = elem.split('</loc>')

        out_url_list.append(url[0])

        open(out_file, 'a').write(url[0] + '\n')

        print(url[0])
