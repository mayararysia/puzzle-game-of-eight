# -*- coding: utf-8 -*-
from search import Search
from node import Node
import os

BLANK_SPACE = ' '

class Puzzle:
    def __init__(self, matrix, goal_matrix, search):  # constructor
        self._matrix = matrix
        self._goal_matrix = goal_matrix
        self._search = search
        self._dictionary = Search.getDictionary()
        self._initialState = self.__getInitialStateOfMatrix()
        self._goalState = self.__getGoalState()
    
    def __getInitialStateOfMatrix(self):
        initialState = []
        for row in range(len(self._matrix)):
            for column in range(len(self._matrix[row])):
                initialState.append(self._matrix[row][column])
        return initialState
    
    def __getGoalState(self):
        goal = []
        for row in range(len(self._goal_matrix)):
            for column in range(len(self._goal_matrix[row])):
                goal.append(self._goal_matrix[row][column])
        return goal
    
    def __setGoalState(self, newGoal):
        self._goalState = newGoal
    
    def __setInitialState(self, state):
         self._initialState = state

    def __clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def iterates_matrix(self):
        self.__iterates_array(self._matrix)
    
    def iterates_goal_matrix(self):
        self.__iterates_array(self._goal_matrix)
    
    def __iterates_array(self, array):
        for row in range(len(array)):
            for column in range(len(array[row])):
                print(array[row][column], end=' ')
            print()

    def getMatrixPuzzle(self):
        return self._matrix

    def isMatrixEmpty(self):
        return self._matrix == None

    def isSearchEmpty(self):
        return self._search == None
    
    def __isFrontierEmpty(self, list):
        return list == None or len(list) == 0

    # def BFS(self, initialState, goalTest):
    #     success = True
    #     failure = False
            
    #     frontier = initialState
    #     explored = []
        
    #     while not self.__isFrontierEmpty(frontier) :
    #         state = frontier.pop(0)
    #         explored.append(state)
                
    #         if goalTest(state):
    #             return success
                
    #         for neighbor in state.neighbors():
    #             if neighbor not in frontier U explored:
    #                 frontier.enqueue(neighbor)
            
    #         return failure
    def BFS(self, initialState, goalTest):
        success = True
        failure = False
        
        UP = 1
        DOWN = 2
        LEFT = 3
        RIGHT = 4
        
        frontier = []
        explored = []
        neighbors = []
        
        index_blank_space = initialState.index(BLANK_SPACE)
        
        print('initialState: ', initialState);
        
        for row in initialState:
            node = Node(row, 0)
            frontier.append(node)
        
        print('index_blank_space: ', index_blank_space)
        list = frontier
        
        while not self.__isFrontierEmpty(frontier) :
            
            state = frontier.pop(index_blank_space)
            # state.cost =
            explored.append(state)
            
            index_left = None
            index_right = None
            index_up = None
            index_down = None
            cost_of_path: 3
            
            left = index_blank_space-1
            right = index_blank_space+1
            
            if left > -1 and (left <= 8 and left >= 0):
                index_left = left
            
            if right > -1 and (right <= 8 and right >= 0):
                index_right = right
                            
            up = index_blank_space-cost_of_path
            down = index_blank_space+cost_of_path
            
            if up > -1 and (up <= 8 and up >= 0):
                index_up = up
            
            if down > -1 and (down <= 8 and down >= 0):
                index_up = up
                
            if index_left != None:
                neighbors.append(list[index_left])
            if index_right != None:
                neighbors.append(list[index_right])
            if index_up != None:
                neighbors.append(list[index_up])
            if index_down != None:
                neighbors.append(list[index_down])
            
            if goalTest(state):
                return success
                
            for neighbor in state.neighbors():
                if neighbor not in frontier U explored:
                    frontier.enqueue(neighbor)
            
            return failure

    def start_search(self):

        if not self.isMatrixEmpty() and not self.isSearchEmpty():
            if self._search.value == Search.BREADTH_FIRST.value:
                print()
                self.__start_breadth_first_search()
            else:
                self._search = Search.BREADTH_FIRST
                self.__start_breadth_first_search()

    def __start_breadth_first_search(self):
        print()
        self.iterates_matrix()
        print()
        print('<< {} >>'.format(self._dictionary[self._search]))
        print()
        print()
        print('Move the blank space up, left, right or down.')
        print()
        print('Control strategy: up, left, right or down')
        print('\n\n')
        
        self.BFS(self._initialState, self._goalState)
        
        # function BFS(initialState, goalTest)
        #     return success or failure:
            
        #     frontier: Queue.new(initialState)
        #     explored = Set.now()
            
        #     while not frontier.isEmpty():
            
        #         state = frontier.dequeue()
        #         explored.add(state)
                
        #         if goalTest(state):
        #             return Sucess (state)
                
        #         for neighbor int state.neighbors():
        #             if neighbor not in frontier U explored:
        #                 frontier.enqueue(neighbor)
        #     return failure
