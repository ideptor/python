class Block:

    blocks = [ 
        [
            [1,1],
            [1,1]
        ],
        [
            [1,1],
            [0,1],
            [0,1]
        ],
        [
            [1,1],
            [1,0],
            [1,0]
        ],
        [
            [0,1],
            [1,1],
            [0,1]
        ],
        [
            [0,1],
            [1,1],
            [1,0]
        ],
        [
            [1,0],
            [1,1],
            [0,1]
        ],
        [
            [0,1],
            [0,1],
            [0,1],
            [0,1]
        ],
    ]

    def __init__(self, shape_idx:int):
        if shape_idx >= len(self.blocks):
            shape_idx = 0
        self.shape_idx = shape_idx

    def show(self):
        return self.blocks[self.shape_idx]