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
            [0,1],
            [0,1],
            [0,1],
            [0,1]
        ],
    ]

    
    # when
    # then
    for i in range(len(show_blocks)):
        b = Block(i)
        assert b.show() == show_blocks[i]
