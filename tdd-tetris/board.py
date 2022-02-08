from block import Block

class Board:
    
    def __init__(self, lines:int = 10):
        self.lines = lines
        self.matrix = [[0]*10 for _ in range(lines)]

    def show(self):
        return self.matrix