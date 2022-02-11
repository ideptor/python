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
        
    def show(self) -> list:
        return self.blocks[self.shape_idx][self.rotate_idx]

    def reset(self, shape_idx:int = -1):
        self.rotate_idx = 0
        self.__change_shape(shape_idx)

    def get_height_width(self) -> tuple:
        cur = self.blocks[self.shape_idx][self.rotate_idx]
        height = len(cur)
        width = len(cur[0])
        return height, width

    def rotate(self, direction:int=1):
        self.rotate_idx += direction
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
                [3,3,3],
                [0,0,3],
            ],
        ],
        [
            [
                [0,4],
                [4,4],
                [0,4]
            ],
            [
                [0,4,0],
                [4,4,4],
            ],            
            [
                [4,0],
                [4,4],
                [4,0]
            ],
            [
                [0,4,0],
                [4,4,4],
            ],

        ],
        [
            [
                [0,5],
                [5,5],
                [5,0]
            ],
            [
                [5,5,0],
                [0,5,5],
            ],
        ],
        [
            [
                [6,0],
                [6,6],
                [0,6]
            ],
            [
                [0,6,6],
                [6,6,0],
            ],
        ],
        [
            [
                [7],
                [7],
                [7],
                [7]
            ],
            [7,7,7,7]
        ],
    ]
