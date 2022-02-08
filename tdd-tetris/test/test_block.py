from block import Block

def test_block_show():
    
    # given
    show_blocks = [
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
            [1],
            [1],
            [1],
            [1]
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

