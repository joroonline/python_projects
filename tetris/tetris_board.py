#! /usr/bin/env python3


class Tetris_board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
    
    def print_board(self):
        print('\033c', end='')
        print('+' + '-' * (self.width * 2 + 1) + '+')
        for row in self.board:
            print('| ' + ' '.join(row) + ' |')
        print('+' + '-' * (self.width * 2 + 1) + '+')
    
    def place_figure(self, figure, x, y):
        for row in range(len(figure)):
            for col in range(len(figure[row])):
                if figure != ' ':
                    self.board[y + row][x + col] = figure[row][col] 