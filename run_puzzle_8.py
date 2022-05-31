# -*- coding: utf-8 -*-
# Jogo dos Oito - Racha Cuca - puzzle-game-of-eight --- Mayara Rysia
from time import sleep
from random import randint
import os
from search import Search
from puzzle import Puzzle


# Two-dimensional lists (arrays) / matrices
matrix_puzzle = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

goal_matrix_puzzle = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

BLANK_SPACE_CODE = 0
BLANK_SPACE = ' '

# Limpa tela no sistema operacional linux ou windows


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def header_message():
    print("\t\tBEM VINDO AO JOGO DOS OITO! / WELCOME TO PUZZLE EIGHT!\n")


def header_game_message():
    print("\t\t<< GAME PUZZLE EIGHT >>\n")


def iterates_matrix(array, isSleepEffect):
    for row in range(len(array)):
        if isSleepEffect:
            sleep(0.5)
        for column in range(len(array[row])):
            print(array[row][column], end=' ')
        print()


def print_model_matrix(isSleepEffect):
    MATRIX = [
        ['[-]', '[-]', '[-]'],
        ['[-]', '   ', '[-]'],
        ['[-]', '[-]', '[-]']
    ]
    iterates_matrix(MATRIX, isSleepEffect)
    print()
    print('Goal State')
    print()
    iterates_matrix(goal_matrix_puzzle, isSleepEffect)
    print()


def repeat_messages_initial_settings(isSleepEffect):
    header_message()
    print("\n\tRealize a configuração Inicial da matriz  / Input the initial configuration of the puzzle matrix")
    print("\n\tPara isso, insira 8 números de 1 a 8, e 0 para o espaço em branco da configuração desejada /"
          "\n To do this, enter 8 numbers from 1 to 8, and 0 for the blank of the desired configuration.\n")
    print_model_matrix(isSleepEffect)


def isElementIntoMatrixPuzzle(number):
    return any(number in x for x in matrix_puzzle)


def initial_design():
    header_message()
    sleep(2)
    print("\t\tAre you ready?\n")
    sleep(2)
    print("\t\tLet's go!!")
    sleep(1)
    clear()
    repeat_messages_initial_settings(True)

    for row in range(len(matrix_puzzle)):
        for column in range(len(matrix_puzzle[row])):
            stop = False

            while not stop:

                sleep(0.5)
                clear()
                repeat_messages_initial_settings(False)

                number = int(
                    input('Enter the number of position [{}][{}]: '.format(row, column)))

                if number == BLANK_SPACE_CODE and not isElementIntoMatrixPuzzle(BLANK_SPACE_CODE):
                    matrix_puzzle[row][column] = BLANK_SPACE_CODE
                    stop = True
                elif (number <= 8 and number >= 1) and not isElementIntoMatrixPuzzle(number):
                    matrix_puzzle[row][column] = number
                    stop = True
                else:
                    print('\n{} is invalid number! Try again.'.format(number))
                    print('\nYour current puzzle: ')
                    iterates_matrix(matrix_puzzle, False)
                    sleep(1)

    print('\nNice job!! ')
    print()
    iterates_matrix(matrix_puzzle, True)
    print()


def play_it():
    stop = False
    search = Search.BREADTH_FIRST
    dictionary = Search.getDictionary()

    while not stop:
        sleep(0.5)
        clear()
        header_game_message()

        iterates_matrix(matrix_puzzle, False)
        print()

        print('\nChoose a search algorithm: ')
        print()
        print('{} - {}'.format(Search.BREADTH_FIRST.value,
              dictionary[Search.BREADTH_FIRST]))
        # print('{} - Depth-first search (DFS)'.format(Search.DEPTH_FIRST.value))
        # print('{} - Greedy search'.format(Search.GREEDY.value))
        # print('{} - A* search'.format(Search.A_START.value))
        print()
        try:
            option = int(input('Option: '))

            if option != None and Search(option) in Search:
                stop = True
                search = Search(option)

        except Exception as error:
            print()
            print('Error. Try again! {}'.format(error))
            sleep(2)
            pass
    print()
    print('Nice job!')

    sleep(2)
    clear()
    header_game_message()

    puzzle_8 = Puzzle(matrix_puzzle, goal_matrix_puzzle,  search)
    
    #puzzle_8 = Puzzle([[1,2,5], [3,4,0], [6, 7, 8]], goal_matrix_puzzle,  search)
    
    #puzzle_8 = Puzzle([[1,0,2], [3,4,5], [6, 7, 8]], goal_matrix_puzzle,  search)
    puzzle_8.start_search()


if __name__ == '__main__':
    clear()
    initial_design()
    sleep(1)
    play_it()
