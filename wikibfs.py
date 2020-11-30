from webscraper import WIKI_PREFIX
import time
import json
import os
from bs4 import BeautifulSoup
import requests
import re


FILENAME = 'wikidata.json'

class WikiGraph(object):
    def __init__(self):
        self.graph = dict() #graph of keys:values where values are list types
        self.visited = dict()

    def wiki_bfs(self, s, destination): #do BFS given source node as link and destination link
        def savedata(s, links, filename = FILENAME):
            try:
                with open(filename) as savefile1:
                    data = json.load(savefile1)
                    data[s] = links
                with open(filename, 'w') as savefile2:
                    json.dump(data, savefile2, indent = 2)

            except FileNotFoundError:
                edata = {s : links}
                with open(filename, 'w') as newsavefile:
                        json.dump(edata, newsavefile, indent = 2)

        queue = []
        self.visited = {s:True} #visited dictionary to track which nodes are visited
        queue.append(s)
        self.addEdges(s)  #neighbor links of source_node
        start_time = time.time()
        layer = 0

        try:
            with open(FILENAME) as jsonfile:
                jsondata = json.load(jsonfile)
        except FileNotFoundError:
            print('Data file not found. Creating one...')

        while queue:
            print('#' * 100)
            print(s)
            print(f"Moving from layer {layer} to {layer + 1}...")
            print('#' * 100)
            layer += 1

            for link in self.graph[s]: #each link in webscrape(s)   ##possible to refactor this into a map function?

                if link not in self.visited: #hasn't been visited and not recorded
                    print(link)
                    self.visited[link] = True
                    queue.append(link)
                    try:
                        if link in jsondata:
                            self.graph[link] = jsondata[link]
                            print(f'Pulled from {FILENAME}')
                        else:
                            self.addEdges(link)
                    except:
                        self.addEdges(link)

                    savedata(link, self.graph[link]) #save to json

                    if destination in self.graph[link]:
                        print(
                            f'Process finished with exit code 1: Breadth First Search Completed. Layers: {layer} Time: {round(time.time() - start_time, 3)}')
                        return
                    elif destination == link:  # check if destination is reached
                        print(f'Process finished with exit code 2: Breadth First Search Completed. Layers: {layer} Time: {round(time.time() - start_time, 3)}')
                        return
            s = queue.pop(0)

    def addEdges(self,p): #adds a neighborlink set from webscrape function v to page p
        self.graph[p] = self.webscrape(p)

    def webscrape(self, url):  # takes wiki url and returns set of all the links
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        # print(soup.prettify())

        links = soup.find_all('a', href=True)  # filter html for href links
        # print(links)
        final_links = []
        for link in links:  # extract links with regex
            linkregex = re.compile(r'href="(\w|/)+"')
            final_link = linkregex.search(str(link))
            if final_link is not None and final_link not in self.visited:
                # print(final_link.group())
                final_links.append(f'{WIKI_PREFIX}{final_link.group()[6:-1]}')
        final_links = list(set(final_links))  # rid duplicates
        final_links.remove(f'{WIKI_PREFIX}/wiki/Main_Page')  # rid unnecessary link
        # print(final_links,len(final_links))
        return final_links
