from board import Board, Direction

EMPTY_LINE = [0 for _ in range(10)]

def test_set_cur_block():

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
    assert board.block.shape_idx == 0
    assert board.block.rotate_idx == 0
    assert board.block_x == 4
    assert board.block_y == 0
    assert board.show() == board_matrix

def test_move_down():

    # given
    before = [
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        EMPTY_LINE
    ]
    after = [
        EMPTY_LINE,
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
    ]
    board = Board(3)
    board.set_cur_block(0)
    assert board.show() == before

    # when
    board.move_block(Direction.DOWN)

    # then
    assert board.show() == after    
