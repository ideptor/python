from board import Board

def test_create_board():

    
    # given
    lines = 11
    empty_bload = [[0]*10 for _ in range(lines)]

    # when
    board = Board(lines)
    matrix = board.show()

    # then
    assert matrix == empty_bload



