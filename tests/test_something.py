# import words_list from gallows
# import pytest

# def test_passing():
#     assert (1, 2, 3) == (1, 2, 3)

#     проверка что в списке слова
test_list=('skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage')
def test_words_list():
    for i in range(len(test_list)):
        assert isinstance(test_list[i], str)



# проверка, что функция вернет слово из списка
# def test_getRandomWord():
#     pass
# проверка функции playAgain
# def test_playAgain():
#     pass
# проверка функции displayBoard
# def test_displayBoard():
#     pass