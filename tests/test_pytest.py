import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from hangman import get_word, get_hide_word, check_letter


# Тест выбора слова
def test_word_choice(word_gen):
    word = get_word()
    assert word.lower() in word_gen


# Тест скрытия слова
def test_hide_word(word_gen):
    result = get_hide_word(word_gen[0])
    assert result


def test_letter_positive(word_gen):
    result = check_letter('s', word_gen[0])
    assert result