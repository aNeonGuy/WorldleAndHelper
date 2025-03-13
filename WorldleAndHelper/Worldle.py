from random import choice as ch


print('Hello! / Привет!')
print('Its a Worldle! / Это Worldle!')
print('An analogue of Wordly. / Аналог Wordly.')
print('Worldle has 2 languages: / В Worldle есть 2 языка:')
print('Russian and English. / Русский и английский.')
print('You need to guess the word. / Вам нужно угадать слово.')
print('You type your guess, / Вы вводите свою догадку,')
print('if some of the letters / если некоторые буквы')
print('in word on correct possition / в слове на правильной позиции')
print('you will see them. / Вы их увидите.')
print('If its not on correct possition / Если они не на правильной позиции')
print('they will be in special list. / Они будут в специальном списке.')
print('If this letter not in word / Если этой буквы нет в слове')
print('it will be in anouther list / она будет в другом списке')
print('If you success to guess the word / Если вам удастся угадать слово')
print('in 6 attempts, you win. / за 6 попыток, вы победили.')
print('Thats it / Вот и все')
print('Good luck! / Удачи!')
print('')
answ = 'VLP'
while answ != 'Exit':
    print('Choose language(type number): / Выберите язык(ведите цифру):')
    print('1 Russian / Русский')
    print('2 English / Английский')
    lang = input()
    word = 'VLP'
    if str(lang) == '1':
        with open('russian.dict', encoding='utf-8') as words:
            word = ch(words.read().split())
    elif str(lang) == '2':
        with open('english.dict') as words:
            word = ch(words.read().split())
    letts_not_in_word = []
    letts_in_word = []
    length = len(word)
    emit = '_' * length
    success = False
    print('So, thats where game starts! / Здесь начинается игра!')
    print('Your mask of word: / Маска вашего слова:')
    print(f'{emit} (word leght {length} / длина слова {length})')
    print('Type guess(word): / Введите догадку(слово):')
    guess = input()
    for attempts in range(6):
        print(f'You have {attempts} attempts/ У тебя {attempts} попыток')
        for index in range(length):
            if guess[index] == word[index]:
                emit_list = list(emit)
                emit_list[index] = word[index]
                emit = ''.join(emit_list)
            if guess[index] in word and word.rfind(guess[index]) != guess[index] and guess[index] not in letts_in_word:
                letts_in_word.append(guess[index])
            if guess[index] in word and list(word).count(guess[index]) == list(emit).count(guess[index]):
                letts_in_word.remove(guess[index])
            if guess[index] not in word:
                letts_not_in_word.append(guess[index])
        if emit == word.strip():
            success = True
            break
        print('letters you have: / Буквы, которые у вас есть')
        print(emit)
        print('letters in word not on correct possition: / Буквы на неправельных позициях')
        print(letts_in_word)
        print('letters not from word: / Буквы не из слова')
        print(letts_not_in_word)
        guess = input()
    if success:
        print('You win!!! Congrats! / Вы победили! Поздравляю!')
    else:
        print(f'You lost. "{word}" was the correct one. / Вы проиграли. "{word}" было ответом.')
    print('If you want to play another time / Если хотите ещё сыграть')
    print('type anything you want / напишите что угодно')
    print('If not, type "Exit". / Если нет, введите "Exit"')
    answ = input()
print('Thank you for using me! / Спасибо за использование!')
print('Bye! It was the "Worldle". / Пока! Это был "Worldle".')
print('')
print('by Neon')
