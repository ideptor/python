from block import Block

def test_block0_show():

    # given
    # when
    b = Block(0)

    # then
    assert b.show() == [[1,1],[1,1]]

def test_block1_show():

    # given
    # when
    b = Block(1)

    # then
    assert b.show() == [ [1,1]
                        ,[0,1]
                        ,[0,1]]
