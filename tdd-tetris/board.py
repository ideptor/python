from block import Block

class Board:
    
    def __init__(self, lines:int = 10):
        self.lines = lines
        self.matrix = [[0]*10 for _ in range(lines)]
        self.block = Block()
        self.block_x = 0
        self.block_y = 0

    def show(self):
        return self.matrix

    def set_cur_block(self, block_shape_idx:int=-1):
        self.block_y = 0
        self.block_x = int((10 - self.block.width) / 2)
        self.cur_block.init(block_shape_idx)

