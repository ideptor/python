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

    # when & then - right
    board.set_cur_block(0)
    assert board.show() == before
    board.move_block(Direction.RIGHT)
    assert board.show() == right


def test_not_move_at_edge():

    # given
    down = [
        EMPTY_LINE,
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
    ]
    left = [
        [1,1,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0],
        EMPTY_LINE
    ]
    right = [
        [0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,1,1],
        EMPTY_LINE
    ]
    board = Board(3)

    # when & then - down
    board.set_cur_block(0)
    board.move_block(Direction.DOWN)

    assert board.show() == down
    board.move_block(Direction.DOWN)
    assert board.show() == down


    # when & then - left
    board.set_cur_block(0)
    for _ in range(4):
        board.move_block(Direction.LEFT)

    assert board.show() == left
    board.move_block(Direction.LEFT)
    assert board.show() == left

    # when & then - right
    board.set_cur_block(0)
    for _ in range(4):
        board.move_block(Direction.RIGHT)
    assert board.show() == right
    board.move_block(Direction.RIGHT)
    assert board.show() == right


def test_not_move_left_where_alreay_filled():
    
    # given
    fixed = [       
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
    ]
    showed = [
        [0,0,0,0,2,2,0,0,0,0],
        [0,0,0,0,1,2,0,0,0,0],
        [0,0,0,0,1,2,0,0,0,0],
    ]
    board = Board(3)
    board.fixed = fixed
    board.set_cur_block(1)

    assert board.show() == showed

    # when
    board.move_block(Direction.LEFT)

    # then
    assert board.show() == showed  # not moved