from block import Block

def test_block0_shape():

    # given
    # when
    b = Block()

    # then
    assert b.shape() == [[1,1],[1,1]]
