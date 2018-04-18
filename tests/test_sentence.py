import pytest

from randomsentence.sentence import Sentence

sentence = Sentence()


@pytest.mark.repeat
def test_init_and_generate():
    """
    Sentence.generate is inside __init__

    2 seconds per call
    :return:
    """
    Sentence()


@pytest.mark.repeat
def test_random():
    """
    1.6 seconds per call
    :return:
    """
    random_sentence = sentence.random()
    assert isinstance(random_sentence, str)


@pytest.mark.repeat
def test_with_rating():
    rated_sentence = sentence.with_rating()

    for pair in rated_sentence['rating']:
        assert len(pair) == 2

    assert isinstance(rated_sentence['sentence'], str)


if __name__ == '__main__':
    pytest.main(['--count=50', '-m', 'repeat', __file__])
    # from timeit import timeit
    #
    # print(timeit(test_random, number=50)/50)
