from block import Block

def test_block_show():
    
    # given
    show_blocks = [
        [
            [1,1],
            [1,1]
        ],
        [
            [2,2],
            [0,2],
            [0,2]
        ],
        [
            [3,3],
            [3,0],
            [3,0]
        ],
        [
            [0,4],
            [4,4],
            [0,4]
        ],
        [
            [0,5],
            [5,5],
            [5,0]
        ],
        [
            [6,0],
            [6,6],
            [0,6]
        ],
        [
            [7],
            [7],
            [7],
            [7]
        ],
    ]

    
    # when
    # then
    for i in range(len(show_blocks)):
        b = Block(i)
        assert b.show() == show_blocks[i]


def test_rotate():
    
    # given
    block1 = [
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
    ]

    #when
    b = Block(1)

    # then
    for idx in range(10):
        assert b.show() == block1[idx%len(block1)]
        b.rotate()


def test_random_block():
    
    # given
    # when
    b = Block()

    # then
    assert len(b.blocks) > 0
    assert b.shape_idx >= 0
    assert b.shape_idx < len(b.blocks)


def test_block_height_width():

    # given
    b = Block(1)

    # when
    # then
    assert b.get_height_width() == (3,2)

    b.rotate()
    assert b.get_height_width() == (2,3)