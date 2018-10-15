

def shortest_word_distance_iter(iterable, word1, word2):
    """
    Returns the minimum distance of 2 words in an iterable of words.

    Examples:
        >>> shortest_word_distance_iter('Where are you going?'.split(), 'are', 'you')
        ... 0
        >>> shortest_word_distance_iter('a brand new bike is still a new bike'.split(), 'a', 'bike')
        ... 1
    """
    min_distance = None
    cur_distance = None
    for word in iterable:
        if cur_distance is not None:
            cur_distance += 1
        if word == word1:
            cur_distance = 0
        elif word == word2:
            if cur_distance is None:
                continue
            min_distance = min(min_distance, cur_distance - 1) if min_distance else cur_distance - 1
    return min_distance


def shortest_word_distance(fp, word1, word2):
    """
    Returns shortest distance of (word1, word2) that was found in fp file.
    """
    def file_words():
        for line in fp:
            for word in line.split():
                yield word
    return shortest_word_distance_iter(file_words(), word1, word2)
