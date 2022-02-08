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

def test_move():

    # given
    before = [
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        EMPTY_LINE
    ]
    down = [
        EMPTY_LINE,
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
    ]
    left = [
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        EMPTY_LINE
    ]
    right = [
        [0,0,0,0,0,1,1,0,0,0],
        [0,0,0,0,0,1,1,0,0,0],
        EMPTY_LINE
    ]

    board = Board(3)

    # when & then - down
    board.set_cur_block(0)
    assert board.show() == before
    board.move_block(Direction.DOWN)
    assert board.show() == down

    # when & then - left
    board.set_cur_block(0)
    assert board.show() == before
    board.move_block(Direction.LEFT)
    assert board.show() == left

    # when & then - left
    board.set_cur_block(0)
    assert board.show() == before
    board.move_block(Direction.RIGHT)
    assert board.show() == right

