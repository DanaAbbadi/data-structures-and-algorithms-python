from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

def testHappyPath():
    actual=insertShiftArray([1,2,4,5], 3)
    expected=[1,2,3,4,5]
    assert actual == expected

def testExpectedFailure():
    actual=insertShiftArray([5,2,7,3], 3)
    expected=[3,5,2,7,3]
    assert actual == expected


def testExpectedFailure2():
    actual=insertShiftArray([2,2,2,2], 5)
    expected=[2,2,2,5,2]
    assert actual == expected

def testEdgeCase():
    actual=insertShiftArray([0,0,9,9], 5)
    expected=[0,0,5,9,9]
    assert actual == expected