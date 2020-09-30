from data_structures_and_algorithms.challenges.left_join.left_join import *


def test_simple_left_join():

    d1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher'}
    d2 = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}

    assert left_join(d1,d2) == [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['outfit', 'garb', 'Null'], ['guide', 'usher', 'follow']]

def test_no_common_keys():
    d1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher'}
    d2 = {'see':'look','talk':'speak','yes':'no','chair':'table'}

    assert left_join(d1,d2) == [['fond', 'enamored', 'Null'], ['wrath', 'anger', 'Null'], ['diligent', 'employed', 'Null'], ['outfit', 'garb', 'Null'], ['guide', 'usher', 'Null']]


def test_1st_dict_is_empty():
    d1 = {}
    d2 = {'see':'look','talk':'speak','yes':'no','chair':'table'}
    
    assert left_join(d1,d2) == []


def test_2nd_dictionary_empty():

    d1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher'}
    d2 = {}

    assert left_join(d1,d2) == [['fond', 'enamored', 'Null'], ['wrath', 'anger', 'Null'], ['diligent', 'employed', 'Null'], ['outfit', 'garb', 'Null'], ['guide', 'usher', 'Null']]
