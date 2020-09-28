from data_structures_and_algorithms.challenges.repeated_word.repeated_word import repeated_word
import pytest

def test_normal_string():
    string = 'Once upon a time, there was a brave princess who...'
    assert repeated_word(string) == 'a'

def test_anothor_regular_string():
    string = 'Hello, my name is Dana. What id your name ?'
    assert repeated_word(string) == 'name'

def test_punctuation_marks():
    string = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    assert repeated_word(string) == 'summer'

def test_capital_words():
    string = 'Good morning, it feels good to see you again'
    assert repeated_word(string) == 'good'

def test_more_than_one_repeated_word():
    string = 'Once upon a time, there was a brave princess in a time...'
    assert repeated_word(string) == 'a'

def test_long_string():
    string = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
    assert repeated_word(string) == 'it'

def test_no_repeated_words():
    string = 'Nice to meet you.'
    assert repeated_word(string) == None

def test_not_a_string():
    string = 7
    with pytest.raises(Exception):
        repeated_word(string)