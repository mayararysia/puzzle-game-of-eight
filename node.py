import copy

BLANK_SPACE_CODE = 0

class Node:

    def __init__(self, puzzleProblem):
        self.children = []
        self.cost_of_path = 3
        self.parent = None
        self.puzzle = puzzleProblem  # format one-dimensional
        self.position = 0

    def __isFrontierEmpty(self, frontier):
        isEmpty = False
        if frontier == None:
            isEmpty = True
        if len(frontier) == 0:
            isEmpty = True

        return isEmpty

    def copyArray(self, array):
        newArray = []
        for index in range(len(array)):
            newArray.append(array[index])
        return newArray

    def goalTest(self):
        success = True
        frontier = self.copyArray(self.puzzle)
        INITIAL_POSITION = 0

        while not self.__isFrontierEmpty(frontier):
            state = frontier.pop(INITIAL_POSITION)

            if len(frontier) > 0 and (state > frontier[INITIAL_POSITION]):
                success = False

        return success
    
    def printArrayPuzzle(self, array):
        if len(array) == 9:
            
            two_dimensional = [
                [array[0], array[1], array[2]],
                [array[3], array[4], array[5]],
                [array[6], array[7], array[8]]
            ]
            
            for row in range(len(two_dimensional)):
                for column in range(len(two_dimensional[row])):
                    print(two_dimensional[row][column], end=' ')
                print()
        else:
            two_dimensional = []
            print(two_dimensional)

    def goRight(self, puzzle, index):

        if (index % self.cost_of_path) < (self.cost_of_path - 1):
            # copy = self.copyArray(puzzle)
            copy = puzzle
            right = index + 1

            state_right = copy[right]
            copy[right] = copy[index]
            copy[index] = state_right

            child = Node(copy)
            copyChild = Node(copy)
            
            self.children.append(child)
            copyChild.setParent(child)
            
            print()
            print('Go Right\n')
            self.printArrayPuzzle(copy)

    def goLeft(self, puzzle, index):

        if (index % self.cost_of_path) > 0:
            # copy = self.copyArray(puzzle)
            copy = puzzle
            left = index-1

            state_left = copy[left]
            copy[left] = copy[index]
            copy[index] = state_left

            child = Node(copy)
            copyChild = Node(copy)
            self.children.append(child)

            copyChild.setParent(child)
            
            print()
            print('Go Left\n')
            self.printArrayPuzzle(copy)


    def goUp(self, puzzle, index):
        if (index - self.cost_of_path) >= 0:
            # copy = self.copyArray(puzzle)
            copy = puzzle
            up = index-self.cost_of_path

            state_up = copy[up]
            copy[up] = copy[index]
            copy[index] = state_up

            child = Node(copy)
            copyChild = Node(copy)

            self.children.append(child)
            copyChild.setParent(child)
           
            child.parent = this;
            
            print()
            print('Go Up\n')
            self.printArrayPuzzle(copy)


    def goDown(self, puzzle, index):
        if (index + self.cost_of_path) < len(puzzle):
             # copy = self.copyArray(puzzle)
            copy = puzzle
            down = index+self.cost_of_path

            state_down = copy[down]
            copy[down] = copy[index]
            copy[index] = state_down

            child = Node(copy)
            copyChild = Node(copy)

            self.children.append(child)

            copyChild.setParent(child)
            
            print()
            print('Go down\n')
            self.printArrayPuzzle(copy)

    def printPuzzle(self):
        if len(self.puzzle) == 9:

            two_dimensional = [
                [self.puzzle[0], self.puzzle[1], self.puzzle[2]],
                [self.puzzle[3], self.puzzle[4], self.puzzle[5]],
                [self.puzzle[6], self.puzzle[7], self.puzzle[8]]
            ]

            for row in range(len(two_dimensional)):
                for column in range(len(two_dimensional[row])):
                    print(two_dimensional[row][column], end=' ')
                print()
        else:
            two_dimensional = []
            print(two_dimensional)

    def isEqualPuzzle(self, puzzle):
        equal = True
        for index in range(len(puzzle)):
            if self.puzzle[index] != puzzle[index]:
                equal = False
        return equal
    
    def find_position_move(self):
         for index in range(len(self.puzzle)):
            if self.puzzle[index] == BLANK_SPACE_CODE:
                self.position = index

    def goExpandNode(self):
        self.find_position_move()
        self.goUp(self.puzzle, self.position)
        
        self.find_position_move()
        self.goLeft(self.puzzle, self.position)
        
        self.find_position_move()
        self.goLeft(self.puzzle, self.position)

    def getPuzzle(self):
        return self.puzzle

    def setPuzzle(self, newPuzzle):
        self.puzzle = newPuzzle

    def getChildren(self):
        return self.children

    def setChildren(self, newValue):
        self.children = newValue

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent
