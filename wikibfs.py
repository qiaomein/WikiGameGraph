from webscraper import webscrape
import time

class WikiGraph(object):
    def __init__(self):
        self.graph = dict() #graph of keys:values where values are list types

    def wiki_bfs(self, s, destination): #do BFS given source node as link and destination link
        queue = []
        visited = {s:True} #visited dictionary to track which nodes are visited
        queue.append(s)
        self.addEdges(s)  #neighbor links of source_node
        start_time = time.time()
        destination_tag = webscrape(destination)
        flag = False

        if destination_tag == self.graph[s]:
            print('You are already on this page!')
            return

        while queue:
            # print(s)
            print("Next Node")
            for link in self.graph[s]: #each link in webscrape(s)   ##possible to refactor this into a map function?
                if link not in visited: #hasn't been visited
                    print(link)
                    visited[link] = True
                    queue.append(link)
                    self.addEdges(link)
                    if destination_tag == self.graph[link]:  # check if destination is reached
                        print(f'Breadth First Search Completed. Time: {round(time.time() - start_time, 3)}')
                        flag = True
                        break
            if flag:
                break
            s = queue.pop(0)

    def addEdges(self,p): #adds a neighborlink set from webscrape function v to page p
        self.graph[p] = webscrape(p)
