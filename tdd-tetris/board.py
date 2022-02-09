from block import Block
import copy
from enum import Enum


class Direction(Enum):
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Board:

    __MAX_WIDTH = 10
    
    def __init__(self, lines:int = 10):
        self.lines = lines
        self.fixed = [[0]*10 for _ in range(lines)]
        self.block = Block(0)
        self.block_x = 0
        self.block_y = 0

    def show(self):
        showed = copy.deepcopy(self.fixed)
        block_matrix = self.block.show()
        height, width = self.block.get_height_width()
        for dy in range(height):
            for dx in range(width):
                showed[self.block_y+dy][self.block_x+dx] += \
                    block_matrix[dy][dx]

        return showed

    def set_cur_block(self, block_shape_idx:int=-1):
        self.block.reset(block_shape_idx)
        self.block_y = 0
        self.block_x = int((10 - self.block.width) / 2)
        
    def move_block(self, direction: Direction):

        height, width = self.block.get_height_width()

        if direction == Direction.DOWN:
            if self.block_y + height >= self.lines:
                return
            self.block_y += 1

        elif direction == Direction.LEFT:
            if self.block_x <= 0:
                return
            if self.__detect_collision(self.block_y, self.block_x-1):
                return
            self.block_x -= 1

        elif direction == Direction.RIGHT:
            if self.block_x + width >= self.__MAX_WIDTH:
                return
            if self.__detect_collision(self.block_y, self.block_x+1):
                return                
            self.block_x += 1

    def __detect_collision(self, y, x):
        
        #showed = copy.deepcopy(self.fixed)
        block_matrix = self.block.show()
        height, width = self.block.get_height_width()
        for dy in range(height):
            for dx in range(width):
                if self.fixed[y+dy][x+dx] > 0 and \
                    block_matrix[dy][dx] > 0:
                    return True
        
        return False
