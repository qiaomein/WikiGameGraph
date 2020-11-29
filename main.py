from webscraper import webscrape, WIKI_PREFIX
from wikibfs import WikiGraph
import json

if __name__ == '__main__':
    # model with directed graph
    query1 = input('Enter beginning Wiki query: ').replace(' ', '_')
    query2 = input('Enter destination Wiki query: ').replace(' ', '_')
    start = f'https://en.wikipedia.org/wiki/{query1}'
    end = f'https://en.wikipedia.org/wiki/{query2}'
    if WIKI_PREFIX in query1 or WIKI_PREFIX in query2:
        start = query1
        end = query2
    # if webscrape(query2) == webscrape(s) then we are done
    wg = WikiGraph()
    wg.wiki_bfs(start,end)