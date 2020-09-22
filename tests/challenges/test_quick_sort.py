from data_structures_and_algorithms.challenges.quick_sort.quick_sort_basic import quickSort, partition


def test_quickSort_case1():
    arr = [8,5,13,9,90]
    expected = [5, 8, 9, 13, 90]
    n = len(arr)
    quickSort(arr,0,n-1)
    actual = arr
    assert actual == expected

def test_merge_one_element():
    arr = [13]
    expected = [13]
    n = len(arr)
    quickSort(arr,0,n-1)
    actual = arr
    assert actual == expected


def test_merge_empty_arr():
    arr = [ ]
    expected = [ ]
    n = len(arr)
    quickSort(arr,0,n-1)
    actual = arr
    assert actual == expected

def test_quickSorted_arr():
    arr = [15,17,18,20,21,25]
    expected = [15,17,18,20,21,25]
    n = len(arr)
    quickSort(arr,0,n-1)
    actual = arr
    assert actual == expected

def test_merge_reverse_sorted():
    arr = [20,18,12,8,5,-2]
    expected = [-2,5,8,12,18,20]
    n = len(arr)
    quickSort(arr,0,n-1)
    actual = arr
    assert actual == expected

def test_merge_few_uniques():
    arr = [5,12,7,5,5,7]
    expected = [5, 5, 5, 7, 7, 12]
    n = len(arr)
    quickSort(arr,0,n-1)
    actual = arr
    assert actual == expected

def test_merge_nearly_sorted():
    arr = [2,3,5,7,13,11]
    expected = [2, 3, 5, 7, 11, 13]
    n = len(arr)
    quickSort(arr,0,n-1)
    actual = arr
    assert actual == expected






