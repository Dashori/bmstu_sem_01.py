##Лабораторная работа № 11
##Имитировать работу базы данных, используя бинарный файл.
##Запись содержит 3-4 поля. Например, запись "книга" содержит поля "автор", "наименование", "год издания".
##Необходимо сделать меню:
##1. Создание БД.
##2. Добавление записи в БД.
##3. Вывод всей БД.
##4. Поиск записи по одному полю.
##5. Поиск записи по двум полям.
##Для работы с текущей записью используется словарь.
##Автор Чепиго Дарья ИУ7-14Б

import pickle as p
circle=0  ##переменная для бесконечного цикла
lot=0     ##количество строк в созданной базе
n=-1 ##количество полей
num='012345'
while circle!=1:
    print('''Меню:
1. Создание БД.
2. Добавление записи в БД.
3. Вывод всей БД.
4. Поиск записи по одному полю.
5. Поиск записи по двум полям.
0.Выход
''')
    choice=str(input('Введите пункт меню: '))
    if choice not in num:
        choice=input('Введите пункт меню: ')
    else:
        choice=int(choice)
        
    if choice==1:
        filename=input('Введите название файла: ')
        filename=filename+'.bin'
        f=open(filename,'wb')
        n=int(input('Введите количество полей: '))
        if n>0:
            dictionary={}  ##создание образца словаря
        pole=[]  ##список для ключей
        for i in range(n):
            pole.append([])
            pole[i]=input('Введите название поля: ')
            dictionary[pole[i]]=''
        f.close()
        print()
    if choice==2:

        if n==-1:
            dictionary={} ##создание словаря
            pole_1=[]     ##список для ключей
            try:
                filename=input('Введите название файла: ')
                filename=filename+'.bin'
                f=open(filename,'rb')
                first=p.load(f)
                for i in first:
                    pole_1.append(i)
                f.close()
                f=open(filename,'ab')
                for i in range(len(pole_1)):
                    print('Введите поле',pole_1[i],': ',end='')
                    dictionary[pole_1[i]]=input()
                p.dump(dictionary,f)
                f.close()
                print()
            except FileNotFoundError:
                print('Файл не был найден. \n')

                
        else:
            f=open(filename,'ab')
            for i in range(len(pole)):
                print('Введите поле',pole[i],': ',end='')
                dictionary[pole[i]]=input()
            lot+=1
            p.dump(dictionary,f)
            f.close()
            print()
        
    if choice==3:
        if lot==0:
            column=0
            col=0
            try:
                filename=input('Введите название файла: ')
                filename=filename+'.bin'
                f=open(filename,'rb')
                sr=p.load(f)
                k=len(sr)
                for t in sr:
                    print('     ','{:18}'.format(t),end='')
                print('')
                print()
                while True:
                    try:
                        k=p.load(f)
                        for j in k:
                            print('     ','{:18}'.format(k[j]),end='')
                        print('')

                    except EOFError:
                        break

            except FileNotFoundError:
                print('Файл не был найден. \n')
            
        else:  
            f=open(filename,'rb')
            for i in range(n):
                print('     ','{:18}'.format(pole[i]),end='')
            print('')
            print()
            for i in range(lot):
                sr=p.load(f)
                for j in range(n):
                    print('     ','{:18}'.format(sr[pole[j]]),end='')
                print(' ')
            f.close()
            
    if choice==4:  ## Поиск записи по одному полю.
        if n==-1:
            try:
                pole_1=[]
                filename=input('Введите название файла: ')
                filename=filename+'.bin'
                f=open(filename,'rb')
                first=p.load(f)
                for i in first:
                    pole_1.append(i)
                for i in range(len(pole_1)):
                    print(i+1,' . ',pole_1[i],sep='')
                select=int(input('Выберите номер поля для поиска: '))
                select=pole_1[select-1]
                word=input('Введите значение поля: ')
                
                while True:
                    try:
                        k=p.load(f)
                        if k[select]==word:
                            for j in k:
                                print('     ','{:18}'.format(k[j]),end='')
                            print('')

                    except EOFError:
                        break
                    
                f.close()
            except FileNotFoundError:
                print('Файл не был найден. \n')
                
        else:
            print('')
            for i in range(len(pole)):
                print(i+1,' . ',pole[i],sep='')
            select=int(input('Выберите номер поля для поиска: '))
            select=pole[select-1]
            word=input('Введите значение поля: ')
            
            f=open(filename,'rb')
            for i in range(n):
                print('     ','{:18}'.format(pole[i]),end='')
            print('')
                
            for i in range(lot):
                sr=p.load(f)
                if sr[select]==word:
                    for j in range(n):
                        print('     ','{:18}'.format(sr[pole[j]]),end='')
                    print(' ')
            print()
            f.close()
        
    if choice==5:
        if n==-1:
            try:  
                pole_1=[]
                filename=input('Введите название файла: ')
                filename=filename+'.bin'
                f=open(filename,'rb')
                first=p.load(f)
                for i in first:
                    pole_1.append(i)
                    
                for i in range(len(pole_1)):
                    print(i+1,' . ',pole_1[i],sep='')
                select_1=int(input('Выберите номер поля #1 для поиска: '))
                select_1=pole_1[select_1-1]
                word_1=input('Введите значение поля #1 : ')

                for i in range(len(pole_1)):
                    print(i+1,' . ',pole_1[i],sep='')
                select_2=int(input('Выберите номер поля #2 для поиска: '))
                select_2=pole_1[select_2-1]
                word_2=input('Введите значение поля #2: ')
                
                while True:
                    try:
                        k=p.load(f)
                        if k[select_1]==word_1 and k[select_2]==word_2:
                            for j in k:
                                print('     ','{:18}'.format(k[j]),end='')
                            print('')

                    except EOFError:
                        break
                    
                f.close()
            except FileNotFoundError:
                print('Файл не был найден. \n')

        else:
            print('')
            for i in range(len(pole)):
                print(i+1,' . ',pole[i],sep='')
                
            select_1=int(input('Выберите номер поля #1 для поиска: '))
            select_1=pole[select_1-1]
            word_1=input('Введите значение поля #1: ')
            print('')
            for i in range(len(pole)):
                print(i+1,' . ',pole[i],sep='')
            print('')    
            select_2=int(input('Выберите номер поля #2 для поиска: '))
            select_2=pole[select_2-1]
            word_2=input('Введите значение поля #2: ')

            f=open(filename,'rb')
            for i in range(n):
                print('     ','{:18}'.format(pole[i]),end='')
            print('')

            for i in range(lot):
                sr=p.load(f)
                if sr[select_1]==word_1 and sr[select_2]==word_2:
                    for j in range(n):
                        print('     ','{:18}'.format(sr[pole[j]]),end='')
                    print('')
            f.close()
        
    if choice==0:
        break
        
        
