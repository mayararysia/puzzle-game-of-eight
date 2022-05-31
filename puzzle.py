# -*- coding: utf-8 -*-
from operator import contains
from search import Search
from node import Node
import os
from time import sleep

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

    def __isFrontierEmpty(self, frontier):
        return frontier == None or len(frontier) == 0

    def BFS(self, root):
        goal = False
        path_solution = []
        frontier = []
        explored = []

        frontier.append(root)

        while not self.__isFrontierEmpty(frontier) and not goal:
            state = frontier[0]
            explored.append(state)

            state.goExpandNode()
            print()
            print('The Puzzle: ')
            state.printPuzzle()
            sleep(1)
            children = state.getChildren()

            for index in range(len(children)):
                child = children[index]

                if child.goalTest() == True:
                    print()
                    print('Goal found')
                    goal = True

                    self.path_trace(path_solution, child)

                if (not self.contains(frontier, child)) and (not self.contains(explored, child)):
                    frontier.append(child)
        return path_solution

    def path_trace(self, pathList, node):
        print('Tracing path...')

        currentNode = node
        pathList.append(currentNode)
        while currentNode.getParent() is not None:
            currentNode = currentNode.getParent()
            pathList.append(currentNode)

    def contains(self, nodeList, node):
        success = False

        for index in range(len(nodeList)):
            if nodeList[index].isEqualPuzzle(node.getPuzzle()):
                success = True
        return success

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
        print('Control strategy: up, left, right or down')
        print('\n\n')

        root = Node(self._initialState)
        solution = self.BFS(root)

        print()
        print('Nodes expanded: ', len(solution))
        print()
        print('\n\nsolution: ')
        if len(solution) > 0:
            for index in range(len(solution)):
                if len(solution[index].getPuzzle()) > 0:
                    print()
                    solution[index].printPuzzle()
                else:
                    print()
                    print('No solution is found')
        else:
            print()
            print('No solution is found')
