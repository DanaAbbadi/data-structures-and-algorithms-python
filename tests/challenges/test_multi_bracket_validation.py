from data_structures_and_algorithms.challenges.multi_bracket_validation_ch.multi_bracket_validation import multi_bracket_validation


def test_case0_balanced():
    mystr = '[] () {}'
    actual = multi_bracket_validation(mystr)
    expected = True
    assert actual == expected

def test_case1_unbalanced():
    mystr = '[ (){ '
    actual = multi_bracket_validation(mystr)
    expected = False
    assert actual == expected

def test_case2_balanced_entwine():
    mystr = '[{()}]'
    actual = multi_bracket_validation(mystr)
    expected = True
    assert actual == expected

def test_case3_unbalanced_entwine():
    mystr = '[()}]'
    actual = multi_bracket_validation(mystr)
    expected = False
    assert actual == expected

def test_with_extra_char():
    mystr = ' ()[[Extra Characters]]'
    actual = multi_bracket_validation(mystr)
    expected = True
    assert actual == expected

def test_balanced_with_chars():
    mystr = ' {}{Code}[Fellows](())'
    actual = multi_bracket_validation(mystr)
    expected = True
    assert actual == expected

def test_unbalnced_missing():
    mystr = ' (](	'
    actual = multi_bracket_validation(mystr)
    expected = False
    assert actual == expected