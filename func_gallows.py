import random
words_list=('skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage')
# возвращает одно любое слово из списка words_list
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def getGuess(alreadyGuessed):
#Возвращает букву, которую ввел игрок. Эта функция проверяет, что введена
# буква, а не какой-то другой символ
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву:')
        elif guess in alreadyGuessed:
            print ('Вы уже пробовали эту букву. Выберите другую')
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print('Пожалуйста, введите букву латиницы!')
        else:
            return guess

def playAgain():
    print('Хотите попробовать еще раз? ("yes" или "no")')
    return input().lower().startswith('y')
# missedLetters = ''
# correctLetters = ''


