import pytest

from word_distance import word_distance


def test_word_distance():
    assert word_distance(['a', 'black', 'box'], 'a', 'box') == 1


def test_word_distance_multiple():
    assert word_distance(['a', 'black', 'box', 'is', 'in', 'a', 'box'], 'a', 'box') == 0


def test_word_distance_double_end():
    assert word_distance(['a', 'black', 'box', 'is', 'in', 'that', 'box'], 'a', 'box') == 1
