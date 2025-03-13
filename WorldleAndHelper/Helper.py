print('Hello! Its "Helper" for "Worldle"! / Привет! Это "Помощник" для "Worldle"!')
print('To help you, say me the number of language(as in "Worldle"): / Чтобы помочь вам, скажите мне номер языка(как в "Worldle"):')
lang = input()
if str(lang) == '1':
    with open('russian.dict', encoding='utf-8') as words:
        listwords = words.readlines()
elif str(lang) == '2':
    with open('english.dict') as words:
        listwords = words.readlines()
print('Okay, which length of word you have(tуpe number): / Хорошо, какая длина слова у вас(введите число):')
length = int(input())
listwords = list(filter(lambda word: len(word) == length, listwords))
answ = 'restart'
while answ == 'restart':
    print('Now type letters you have in word(in one line, bettwen put space): / Теперь введите буквы, которые у вас есть в слове(в одну строку через пробел):')
    listgletts = input().split()
    for word in listwords:
        if any(map(lambda lett: lett not in word, listgletts)):
            listwords.remove(word)
    print('Now type letters you dont have in word(in one line, bettwen put space): / Теперь введите буквы, которых у вас нет в слове(в одну строку через пробел):')
    listbletts = input().split()
    for word in listwords:
        if any(map(lambda lett: lett in word, listbletts)):
            listwords.remove(word)
    print('I sorted for you all words you can have! / Я отсортировал для вас все слова, которые у вас могут быть!')
    print('Here it is: / Вот они:')
    print(listwords)
    print('Do you have any new info? If yes, type "restart" / У вас есть какая-нибудь новая информация? Если да, введите "restart"')
    print('else anything you want: / иначе все, что захотите:')
answ = input()
print('Thank you for using me! / Спасибо за использование!')
print('Bye! It was the "Helper"!. / Пока! Это был "Helper".')
print('')
print('by Neon')
