from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search_code  import binarySearch

def testSearch():
    expected = 2
    received = binarySearch([2,6,7,8,9],0,4,7)
    assert expected == received

def testFail():
    expected = -1
    received = binarySearch([8,9,1,3,2],0,4,7)
    assert expected == received