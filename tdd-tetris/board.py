from block import Block
import copy
#from enum import Enum


class Position:

    def __init__(self, y:int, x:int):
        self.y = y
        self.x = x

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.y+other.y, self.x+other.x)

class Move:
    DOWN = Position(1,0)
    LEFT = Position(0,-1)
    RIGHT = Position(0,1)

"""
class Direction(Enum):
    DOWN = 1
    LEFT = 2
    RIGHT = 3
"""

class Board:

    __MAX_WIDTH = 10
    
    def __init__(self, lines:int = 10):
        self.lines = lines
        self.fixed = [[0]*10 for _ in range(lines)]
        self.block = Block(0)
        self.block_pos = Position(0,0)

    def show(self) -> list:
        showed = copy.deepcopy(self.fixed)
        block_matrix = self.block.show()
        height, width = self.block.get_height_width()
        for dy in range(height):
            for dx in range(width):
                showed[self.block_pos.y+dy][self.block_pos.x+dx] += \
                    block_matrix[dy][dx]

        return showed

    def set_cur_block(self, block_shape_idx:int=-1):
        self.block.reset(block_shape_idx)
        _, width = self.block.get_height_width()
        self.block_pos = Position(0, int((10 - width) / 2))


    def move_block(self, direction: Move):

        if not self.__boundary_check(self.block_pos + direction):
            return

        if not self.__collision_check(self.block_pos + direction):
            return                                

        self.block_pos += direction

    def __boundary_check(self, pos:Position) -> bool:
        height, width = self.block.get_height_width()
        if pos.x < 0 or \
            pos.x + width > self.__MAX_WIDTH or \
            pos.y + height > self.lines:
            return False

        return True
            

    def __collision_check(self, pos:Position) -> bool:
        
        assert pos is not None
        #showed = copy.deepcopy(self.fixed)
        block_matrix = self.block.show()
        height, width = self.block.get_height_width()
        for dy in range(height):
            for dx in range(width):
                if self.fixed[pos.y+dy][pos.x+dx] > 0 and \
                    block_matrix[dy][dx] > 0:
                    return False
        
        return True
