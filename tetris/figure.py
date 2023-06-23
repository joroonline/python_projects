#! /usr/bin/env python3


class Figure:
    def __init__(self, figure, x, y):
        self.x = x
        self.y = y
        self.figure = figure
    
    def rotation(self):
        self.figure = list(map(list, zip(*self.figure)))
    
    def move_down(self):
        self.y += 1

    def move_right(self):
        self.x += 1
    
    def move_left(self):
        self.x -= 1