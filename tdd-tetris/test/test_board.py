from board import Board, Move, Position

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
    assert board.block_pos == Position(0, 4)
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

    assert board.block_pos.y == 0
    assert board.block.get_height_width()[0] == 2
    assert board.lines == 3
    board.move_block(Move.DOWN)
    assert board.block_pos.y == 1
    
    assert board.show() == down

    # when & then - left
    board.set_cur_block(0)
    assert board.show() == before
    board.move_block(Move.LEFT)
    assert board.show() == left

    # when & then - right
    board.set_cur_block(0)
    assert board.show() == before
    board.move_block(Move.RIGHT)
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
    board.move_block(Move.DOWN)

    assert board.show() == down
    board.move_block(Move.DOWN)
    assert board.show() == down


    # when & then - left
    board.set_cur_block(0)
    for _ in range(4):
        board.move_block(Move.LEFT)

    assert board.show() == left
    board.move_block(Move.LEFT)
    assert board.show() == left

    # when & then - right
    board.set_cur_block(0)
    for _ in range(4):
        board.move_block(Move.RIGHT)
    assert board.show() == right
    board.move_block(Move.RIGHT)
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
    board.move_block(Move.LEFT)

    # then
    assert board.show() == showed  # not moved


def test_not_move_right_where_alreay_filled():
    
    # given
    fixed = [       
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0],
    ]
    showed = [
        [0,0,0,0,3,3,0,0,0,0],
        [0,0,0,0,3,1,0,0,0,0],
        [0,0,0,0,3,1,0,0,0,0],
    ]
    board = Board(4)
    board.fixed = fixed
    board.set_cur_block(2)

    assert board.show() == showed

    # when
    board.move_block(Move.RIGHT)

    # then
    assert board.show() == showed  # not moved    


def test_not_move_down_where_alreay_filled():
    
    # given
    fixed = [       
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,2,2,2,2,0,0,0],
    ]
    showed = [
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,2,2,2,2,0,0,0],
    ]
    board = Board(3)
    board.fixed = fixed
    board.set_cur_block(0)

    assert board.show() == showed

    # when
    board.move_block(Move.DOWN)

    # then
    assert board.show() == showed  # not moved    


def test_fix_block():
    
    # given
    fixed = [       
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,2,2,2,2,0,0,0],
    ]
    showed = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,2,2,2,2,0,0,0],
    ]
    showed2 = [
        [0,0,0,0,3,3,0,0,0,0],
        [0,0,0,0,3,0,0,0,0,0],
        [0,0,0,0,3,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,2,2,2,2,0,0,0],
    ]
    board = Board(7)
    board.fixed = fixed
    board.set_cur_block(0)
    board.block_pos = Position(4,4)

    assert board.show() == showed

    # when
    board.fix_block()
    board.set_cur_block(2)

    # then
    assert board.fixed == showed  
    assert board.show() == showed2

def test_remove_filled():
    # given
    fixed = [       
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [2,2,2,2,2,2,2,2,2,0],
        [0,2,2,2,2,2,2,2,2,0],
        [2,2,2,2,2,2,2,2,0,0],
        [2,2,2,2,2,2,2,2,2,0],
    ]
    showed = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [2,2,2,2,2,2,2,2,2,7],
        [0,2,2,2,2,2,2,2,2,7],
        [2,2,2,2,2,2,2,2,0,7],
        [2,2,2,2,2,2,2,2,2,7],
    ]
    fixed2 = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,2,2,2,2,2,2,2,2,7],
        [2,2,2,2,2,2,2,2,0,7],
    ]
    showed2 = [
        [0,0,0,0,0,4,0,0,0,0],
        [0,0,0,0,4,4,0,0,0,0],
        [0,0,0,0,0,4,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,2,2,2,2,2,2,2,2,7],
        [2,2,2,2,2,2,2,2,0,7],
    ]
    board = Board(7)
    board.fixed = fixed

    board.set_cur_block(6)
    board.block_pos = Position(3,9)
    assert board.show() == showed

    # when
    board.fix_block()
    board.set_cur_block(3)

    # then
    assert len(board.fixed) == 7
    assert board.fixed == fixed2
    assert board.show() == showed2    


def test_not_rotate_boundary_out():
    # given

    showed = [
        [0,0,0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,0,4,4],
        [0,0,0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,0,0,0],
    ]
    board = Board(4)
    board.set_cur_block(3)

    for _ in range(4):
        board.move_block(Move.RIGHT)

    assert board.show() == showed

    # when
    board.rotate_block()

    # then
    assert board.show() == showed  # not rotated
