from fairsharer import fair_sharer

# test multiple max
def test_fair_sharer():
    assert fair_sharer([1000, 0, 1000, 0], 1) == [800, 200, 800, 200]



    