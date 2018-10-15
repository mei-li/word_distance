import io
import pytest

from word_distance import shortest_word_distance_iter, shortest_word_distance


def test_word_distance():
    assert shortest_word_distance_iter(['a', 'black', 'box'], 'a', 'box') == 1


def test_word_distance_multiple():
    assert shortest_word_distance_iter(['a', 'black', 'box', 'is', 'in', 'a', 'box'], 'a', 'box') == 0


def test_word_distance_double_end():
    assert shortest_word_distance_iter(['a', 'black', 'box', 'is', 'in', 'that', 'box'], 'a', 'box') == 1


@pytest.mark.parametrize('word1, word2',[
    ('a', 'not_there'),
    ('not_there', 'box'),
    (None, None),
])
def test_word_distance_not_found(word1, word2):
    assert shortest_word_distance_iter(['a', 'black', 'box'], word1, word2) is None


def test_word_distance_integration():
    assert shortest_word_distance_iter("We do value and reward motivation in our development team. "
                         "Development is a key skill for a DevOp.".split(), 'motivation',
                         'development') == 2


def test_file_word_distance():
    fp = io.StringIO(
        """This is a multiline
           file to find the distance of
           words""")

    assert shortest_word_distance(fp, 'is', 'words') == 8
