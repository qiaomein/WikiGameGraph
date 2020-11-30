from bs4 import BeautifulSoup
import requests
import re
import json

WIKI_PREFIX = 'https://en.wikipedia.org'

# query1=input('Enter a Wiki query: ').replace(' ','_')
# query2=''
# url = f'https://en.wikipedia.org/wiki/{query1}'


def webscrape(url): #takes wiki url and returns set of all the links
    source = requests.get(url).text
    soup = BeautifulSoup(source,'html.parser')
    # print(soup.prettify())

    links = soup.find_all('a',href = True) #filter html for href links
    # print(links)
    final_links=[]
    for link in links: #extract links with regex
        linkregex = re.compile(r'href="(\w|/)+"')
        final_link = linkregex.search(str(link))
        if final_link is not None:
            # print(final_link.group())
            final_links.append(f'{WIKI_PREFIX}{final_link.group()[6:-1]}')
    final_links = list(set(final_links)) #rid duplicates
    final_links.remove(f'{WIKI_PREFIX}/wiki/Main_Page') #rid unnecessary link
    # print(final_links,len(final_links))
    return final_links

# with open('wikidata.json') as jsonfile:
#     jsondata = json.load(jsonfile)
# print(len(webscrape(f'{WIKI_PREFIX}/wiki/stalin')),len(jsondata))

# print(webscrape('https://en.wikipedia.org/wiki/stalin') == \
# webscrape('https://en.wikipedia.org/wiki/Joseph_Stalin'))