from data_structures_and_algorithms.challenges.array_shift.array_shift import insert_shift_array

def test_happy_path():
    actual=insert_shift_array([1,2,4,5], 3)
    expected=[1,2,3,4,5]
    assert actual == expected

def test_expected_failure():
    actual=insert_shift_array([5,2,7,3], 3)
    expected=[3,5,2,7,3]
    assert actual == expected


def test_expected_failure2():
    actual=insert_shift_array([2,2,2,2], 5)
    expected=[2,2,2,5,2]
    assert actual == expected

def test_edge_case():
    actual=insert_shift_array([], 5)
    expected=[5]
    assert actual == expected

def test_edge_case2():
    actual=insert_shift_array([1,2,4], '5')
    expected= [1,2,4]
    assert actual == expected 