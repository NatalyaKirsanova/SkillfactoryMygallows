from func_gallows import getRandomWord, getGuess,words_list,playAgain

def displayBoard(missedletters, correctLetters,secretWord):
    print( len( missedLetters ))
    print()
    print('Неправильные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '-'*len(secretWord)
#Заменяем тире на правильно угаданные буквы
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
#Показываем загаданное слово с пробелами между букв
    for letter in blanks:
        print(letter, end=' ')
    print()
    # print(getRandomWord(words_list))
    # print(getGuess(alreadyGuessed))
print( 'В И С Е Л И Ц А' )
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord( words_list )
gameIsDone = False
alreadyGuessed = ''
while True:
    displayBoard(missedLetters,correctLetters,secretWord)
        # Вычисляем количество букв, которые ввел игрок
    guess = getGuess( missedLetters + correctLetters )
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Проверка условия победы игрока
        foundAllLetters = True
        for i in range( len( secretWord ) ):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print( 'Превосходно! Было загадано слово "' + secretWord + '" Вы победили!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
            # Проверка условия проигрыша игрока
        if len( missedLetters ) == 4:
            displayBoard(missedLetters, correctLetters, secretWord)
            print( 'У вас не осталось попыток!\nПосле ' + str( len( missedLetters ) )
                   + ' ошибок и ' + str( len( correctLetters ) ) + 'угаданных букв. Загаданное слово:'
                   + secretWord + '"' )
            gameIsDone = True
            # Спрашиваем, хочет ли игрок сыграть еще раз.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord( words )
        else:
            break


