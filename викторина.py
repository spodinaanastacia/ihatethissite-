def f():
    spisok = ['Что было до вчера?', 'Что?', 'Где?', 'Кто изображен на третьем компьюторе с конца справа от входа в 314?', 'Какой ответ в 60 задаче сборника по физике?']
    spisok1 = ['позавчера','не знаю','здесь','капибара','2']
    a = 0 
    for i in range(len(spisok)):  # len = длина 
        print(spisok[i])
        answer = input()
        if answer==(spisok1[i]):
            print ("правильно")
            a = a + 1 
            print ('Ваш счет', a)    
        else:
            print ('неправильно')
    print ('Хотите сыграть еще раз?') 
    a = input()
    if a == "да":
        f()
f() 