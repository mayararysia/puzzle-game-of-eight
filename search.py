from enum import Enum


class Search(Enum):
    BREADTH_FIRST = 1
    # DEPTH_FIRST = 2
    # GREEDY = 3
    # A_START = 4
    
    def getDictionary():
        dictionary = {}
        dictionary[Search.BREADTH_FIRST] = 'Breadth-first search (BFS)'
        # dictionary[Search.DEPTH_FIRST] = 'Depth-first search (DFS)'
        # dictionary[Search.GREEDY] = 'Greedy search'
        # dictionary[Search.A_START] = ' A* search'
        return dictionary

