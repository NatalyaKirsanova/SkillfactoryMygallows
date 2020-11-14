# from gallows import getRandomWord
import pytest
from func_gallows import getRandomWord, getGuess,words_list,playAgain

test_list=('skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage')
def test_wordslist():
    for i in range(len(test_list)):
        assert isinstance(test_list[i], str)

# проверка, что функция вернет слово из списка
def test_getRandomWord():
    assert(getRandomWord(test_list) in test_list)

