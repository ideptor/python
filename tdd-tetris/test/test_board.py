from board import Board

EMPTY_LINE = [0 for _ in range(10)]

def test_create_board():

    
    # given
    lines = 11
    empty_bloard_matrix = [[0]*10 for _ in range(lines)]

    # when
    board = Board(lines)
    matrix = board.show()

    # then
    assert matrix == empty_bloard_matrix


""""
def test_set_next_block():

    # given
    board_matrix = [
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        EMPTY_LINE
    ]

    # when
    board = Board(3)
    board.set_cur_block(0)

    # then
    assert board.show() == board_matrix
"""
