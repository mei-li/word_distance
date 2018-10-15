import pytest

from word_distance import word_distance


def test_word_distance():
    assert word_distance(['a', 'black', 'box'], 'a', 'box') == 1


def test_word_distance_multiple():
    assert word_distance(['a', 'black', 'box', 'is', 'in', 'a', 'box'], 'a', 'box') == 0


def test_word_distance_double_end():
    assert word_distance(['a', 'black', 'box', 'is', 'in', 'that', 'box'], 'a', 'box') == 1


@pytest.mark.parametrize('word1, word2',[
    ('a', 'not_there'),
    ('not_there', 'box'),
    (None, None),
])
def test_word_distance_not_found(word1, word2):
    assert word_distance(['a', 'black', 'box'], word1, word2) is None


def test_word_distance_integration():
    assert word_distance("We do value and reward motivation in our development team. "
                         "Development is a key skill for a DevOp.".split(), 'motivation',
                         'development') == 2
