from block import Block
import copy

class Position:

    def __init__(self, y:int, x:int):
        self.y = y
        self.x = x

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.y+other.y, self.x+other.x)

    def __eq__(self, other):
        if self.y == other.y and self.x == other.x:
            return True
        return False

class Move:
    DOWN = Position(1,0)
    LEFT = Position(0,-1)
    RIGHT = Position(0,1)

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

    def __remove_filled(self):
        next_fixed = [[0]*10 for _ in range(self.lines)]
        next_fixed_line = self.lines - 1
        for i in range(self.lines):
            line = self.lines - i - 1
            for b in self.fixed[line]:
                if b == 0:
                    filled = False
                    break
            else:
                filled = True

            if filled == False:
                next_fixed[next_fixed_line] = copy.deepcopy(self.fixed[line])
                next_fixed_line -= 1
        
        self.fixed = next_fixed
        
    def fix_block(self):
        self.fixed = self.show()
        self.__remove_filled()
        self.block.reset()

    def set_cur_block(self, block_shape_idx:int=-1):
        self.block.reset(block_shape_idx)
        _, width = self.block.get_height_width()
        self.block_pos = Position(0, int((10 - width) / 2))

    def rotate_block(self):
        self.block.rotate()
        if not self.__boundary_check(self.block_pos):
            self.block.rotate(-1)
        elif not self.__collision_check(self.block_pos):
            self.block.rotate(-1)            


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
        
        block_matrix = self.block.show()
        height, width = self.block.get_height_width()
        for dy in range(height):
            for dx in range(width):
                if self.fixed[pos.y+dy][pos.x+dx] > 0 and \
                    block_matrix[dy][dx] > 0:
                    return False
        
        return True
