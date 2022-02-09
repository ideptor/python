import random

class Block:

    shape_idx = 0

    def __init__(self, shape_idx:int = -1):
        self.reset(shape_idx)

    def __change_shape(self, shape_idx):
        if shape_idx == -1:
            self.shape_idx = random.randint(0, len(self.blocks)-1)
        elif shape_idx >= len(self.blocks):
            self.shape_idx = 0
        else:            
            self.shape_idx = shape_idx
        
    def show(self):
        return self.blocks[self.shape_idx][self.rotate_idx]

    def reset(self, shape_idx:int = -1):
        self.rotate_idx = 0
        self.__change_shape(shape_idx)

    def get_height_width(self):
        cur = self.blocks[self.shape_idx][self.rotate_idx]
        height = len(cur)
        width = len(cur[0])
        return height, width

    def rotate(self):
        self.rotate_idx += 1
        self.rotate_idx %= len(self.blocks[self.shape_idx])

    blocks = [
        [ 
            [
                [1,1],
                [1,1]
            ],
        ],
        [
            [
                [2,2],
                [0,2],
                [0,2]
            ],
            [
                [0,0,2],
                [2,2,2],
            ],
            [
                [2,0],
                [2,0],
                [2,2]
            ],
                    [
                [2,2,2],
                [2,0,0],
            ],
        ],
        [
            [
                [3,3],
                [3,0],
                [3,0]
            ],
            [
                [3,0,0],
                [3,3,3],
            ],
            [
                [0,3],
                [0,3],
                [3,3]
            ],
                    [
                [1,1,1],
                [0,0,1],
            ],
        ],
        [
            [
                [0,1],
                [1,1],
                [0,1]
            ],
            [
                [0,1,0],
                [1,1,1],
            ],
            [
                [1,0],
                [1,1],
                [1,0]
            ],
            [
                [0,1,0],
                [1,1,1],
            ],
        ],
        [
            [
                [0,1],
                [1,1],
                [1,0]
            ],
            [
                [1,1,0],
                [0,1,1],
            ],
        ],
        [
            [
                [1,0],
                [1,1],
                [0,1]
            ],
            [
                [0,1,1],
                [1,1,0],
            ],
        ],
        [
            [
                [1],
                [1],
                [1],
                [1]
            ],
            [1,1,1,1]
        ],
    ]
