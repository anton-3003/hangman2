import pytest


@pytest.fixture()
def word_gen():
    words = ["skillfactory",
             'testing',
             'blackbox',
             'pytest',
             'unittest',
             'coverage'
             ]
    return words