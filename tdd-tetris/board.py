from block import Block
import copy

class Board:
    
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
        

