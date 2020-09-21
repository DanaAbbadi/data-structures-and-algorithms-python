from data_structures_and_algorithms.challenges.insertion_sort_challenge.insertion_sort import *


def test_insertion_sort_case1():
    arr = [8,5,13,9,90]
    expected = [5, 8, 9, 13, 90]
    actual = insertion_sort(arr)
    assert actual == expected

def test_insertion_one_element():
    arr = [13]
    expected = [13]
    actual = insertion_sort(arr)
    assert actual == expected


def test_insertion_empty_arr():
    arr = [ ]
    expected = [ ]
    actual = insertion_sort(arr)
    assert actual == expected

def test_insertion_sorted_arr():
    arr = [15,17,18,20,21,25]
    expected = [15,17,18,20,21,25]
    actual = insertion_sort(arr)
    assert actual == expected

def test_insertion_reverse_sorted():
    arr = [20,18,12,8,5,-2]
    expected = [-2,5,8,12,18,20]
    actual = insertion_sort(arr)
    assert actual == expected

def test_insertion_few_uniques():
    arr = [5,12,7,5,5,7]
    expected = [5, 5, 5, 7, 7, 12]
    actual = insertion_sort(arr)
    assert actual == expected

def test_insertion_nearly_sorted():
    arr = [2,3,5,7,13,11]
    expected = [2, 3, 5, 7, 11, 13]
    actual = insertion_sort(arr)
    assert actual == expected






