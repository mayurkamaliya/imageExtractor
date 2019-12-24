import re
import requests
from bs4 import BeautifulSoup
import os
import csv

count = 1
with open("links.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        site = row[0]
        os.mkdir("Images of link " + str(count))
        filepath = os.getcwd() + str("/Images of link " + str(count))
        response = requests.get(site)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        urls = [img['src'] for img in img_tags]

        for url in urls:
            filename = re.search(r'/([\w_-]+[.](jpg|png))$', url)
            if filename is not None:
                with open(os.path.join(filepath ,filename.group(1)), 'wb') as f:
                    if 'http' not in url:
                        url = '{}{}'.format(site, url)
                    response = requests.get(url)
                    f.write(response.content)
        print("Downloaded images from link number = " + str(count) )
        count = count + 1
print("Done")