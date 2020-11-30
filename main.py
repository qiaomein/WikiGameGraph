from webscraper import webscrape, WIKI_PREFIX
from wikibfs import WikiGraph
import json

if __name__ == '__main__':
    # model with directed graph

    #fetch urls from user
    query1 = input('Enter beginning Wiki query URL: ')
    query2 = input('Enter destination Wiki query URL: ')
    if WIKI_PREFIX not in query1 or WIKI_PREFIX not in query2:
        print("Enter valid URLs!")
    start = query1
    end = query2
    #create graph
    wg = WikiGraph()
    #run bfs
    wg.wiki_bfs(start,end)