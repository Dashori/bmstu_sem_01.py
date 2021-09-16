##Лабораторная работа №9
##Написать программу, реализующую меню
print('''Пункты Меню:
1. Ввод строки
2. Настройка шифрующего алгоритма
3. Шифрование строки, используя шифр Виженера
4. Расшифровывание строки
''')
circle=0
alphabet='abcdefjhigklmnopqrstuvwxyz '

def define(x):  ##Функция чтоб проверять есть ли в строке символы помимо букв и пробелов
    count=0
    x=x.lower()
    for i in range(len(x)):
        if x[i] in alphabet:  ##подсчет количества букв в символе
            count+=1
    if count==len(x):
        count=1               ##если количество букв совпадает с длиной строки
    else:
        count=0               ##если не совпадает, т.е. просим ввести еще раз
    return(count)
while circle!=1:
    num=str(input('Введите пункт меню: '))
    if num=='1':
        line=str(input(('Введите строку: ')))
        line=line.lower()               ##понижение регистра всех букв
        while define(line)!=1:
            line=str(input('''Строка может состоять только из английских букв и пробелов
Введите еще раз: '''))
        line=line.lower()               ##понижение регистра всех букв
        print()
    if num=='2':
        code=str(input('Введите код шифрования: '))
        code=code.lower()               ##понижение регистра всех букв
        while define(code)!=1:
            code=str(input('''Строка может состоять только из английских букв и пробелов
Введите еще раз: '''))
        code=code.lower()               ##понижение регистра всех букв
        print()
    if num=='3':
        j=0          ##индекс для сдвига кода шифрования
        line_2=''    ##строка для шифрования
        for i in range(len(line)):    ##шифрование строки
            index=(alphabet.index(line[i])+alphabet.index(code[j]))%27
            line_2+=alphabet[index]
            
            if j!=len(code)-1:##цикл для чередования ключа шифрования
                j=j+1
            else:
                j=0
       
        print('Зашифрованная строка: ',line_2)
        print()
        
    if num=='4':
        j=0          ##индекс для сдвига кода шифрования
        line_3=''    ##строка для расшифровки
        for i in range(len(line)):       ##расшифровка строки
            index=(alphabet.index(line_2[i])+27-alphabet.index(code[j]))%27
            line_3+=alphabet[index]
            if j!=len(code)-1: ##цикл для чередования ключа шифрования
                j=j+1
            else:
                j=0
        print('Расшифрованная строка: ',line_3)
        print()
       
