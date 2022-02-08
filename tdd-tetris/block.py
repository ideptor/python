import random

class Block:

    def __init__(self, shape_idx:int = -1):

        if shape_idx == -1:
            self.shape_idx = random.randint(0, len(self.blocks)-1)
        elif shape_idx >= len(self.blocks):
            shape_idx = 0
        else:            
            self.shape_idx = shape_idx
        
        self.rotate_idx = 0

    def show(self):
        return self.blocks[self.shape_idx][self.rotate_idx]

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
                [1,1],
                [0,1],
                [0,1]
            ],
            [
                [0,0,1],
                [1,1,1],
            ],
            [
                [1,0],
                [1,0],
                [1,1]
            ],
                    [
                [1,1,1],
                [1,0,0],
            ],
        ],
        [
            [
                [1,1],
                [1,0],
                [1,0]
            ],
            [
                [1,0,0],
                [1,1,1],
            ],
            [
                [0,1],
                [0,1],
                [1,1]
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
