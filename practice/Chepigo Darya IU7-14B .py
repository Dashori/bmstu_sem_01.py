symb = []     ##сам кроссворд
num = []      ##список для определения порядкового числа слов
number = 1    ##переменная для определения порядкового числа слова
circle = 1    ##переменная для бесконечного цикла
count = 1     ##номер введенного кроссворда
num_row = ['0','1','2','3','4','5','6','7','8','9','10']
num_column = ['1','2','3','4','5','6','7','8','9','10']
alphabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_eng = 'abcdefghijklmnopqrstuvwxyz*'


def define(line): ##функция для проверки, что введена строка букв или *
    counter = 0
    for i in range(len(line)):
        if line[i].lower() in alphabet_rus or line[i].lower() in alphabet_eng:
            counter+=1
        else:
            return False
    if counter == len(line) and len(line) == c:
        return True
    else:
        return False
    
def row(r_1,c_1,num_1,symb_1): ##функция для формирования списка across
    array_1 = []
    for j in range(r_1):
        array_1.append([])
        array_1[j].append([])      
    for i in range(r_1):  
        k = 0
        for j in range(c_1):
            if num_1[i][j] != '*' and num_1[i][j] != '0':
                if len(array_1[i][k]) == 0:
                    array_1[i][k].append(num_1[i][j])
                array_1[i][k].append(symb_1[i][j])
            if num_1[i][j] == '*':
                array_1[i].append([])
                k = k + 1
    return array_1

def column(r_2,c_2,num_2,symb_2):  ##функция для формирования списка down
    array_2 = []
    for i in range(c_2):
        array_2.append([])
        
    for j in range(c_2):
        k = 0
        for i in range(r_2):
            array_2[j].append([])
            if num_2[i][j] != '*' and num_2[i][j] != '0':
                if len(array_2[j][k]) == 0:
                    array_2[j][k].append(num_2[i][j])
                array_2[j][k]+=(symb_2[i][j])
            if num_2[i][j] == '*':
                k = k + 1
    return array_2

def sorting(words): ##функция для сортировки списка по порядковому номеру слова
    array = []
    for  i in range(len(words) - 1,-1,-1):
        for j in range(len(words[i]) - 1,-1,-1):
            if len(words[i][j]) <= 1:
                del words[i][j]
        if len(words[i]) == 0:
            del words[i]
    for i in range(len(words)):
        for j in range(len(words[i])):
            array.append(words[i][j])

    for i in range(len(array) - 1):
        for j in range(len(array) - 2,i - 1,-1):
            if array[j][0] > array[j + 1][0]:
                array[j],array[j + 1] = array[j + 1],array[j]
    return array   


def printout(words_1): ##функция для вывода списка в нужном формате
    for i in range(len(words_1)):
        print('       ',words_1[i][0],'.',end=' ',sep='')
        for k in range(1,len(words_1[i])):
            print(words_1[i][k],end='',sep='')
        print()
        

while circle != 0:
    print('Кроссворд ',count,':')
    r = input('Введите количество строк: ')
    while r not in num_row:
        r = input('Введите число от 1 до 10: ')
    if r == '0':
        break
    
    c = input('Введите количество столбцов: ')
    while c not in num_column:
        c = input('Введите число от 1 до 10: ')
        
    r = int(r)
    c = int(c)

    for i in range(r):
        symb.append([])
        num.append([0] * c)
        print('Введите',i + 1,'строку: ')
        symb[i] = str(input())
        while not define(symb[i]):
            print('Строка должна состоять только из букв и * и иметь длину ',c)
            symb[i] = str(input('Введите еще раз: '))
                   
    for j in range(c): ## проход по первой строке
        if symb[0][j] != '*':
            num[0][j] = number
            number+=1
        else:
            num[0][j] = '*'
            
    for i in range(1,r):  ##проход по остальным строкам
        if symb[i][0] != '*':     ##проверка первого столбца каждой строки
            num[i][0] = number
            number+=1
        else:
            num[i][0] = '*'
        for j in range(1,c):     ##проверка остальных элементов
            if symb[i][j] != '*':
                if symb[i][j - 1] == '*' or symb[i - 1][j] == '*':
                    num[i][j] = number
                    number+=1
                else:
                    num[i][j] = ' '
            else:
                num[i][j] = '*'
    print()
    across = row(r,c,num,symb)
    across = sorting(across)
    down = column(r,c,num,symb)
    down = sorting(down)
    print('puzzle #',count,':',sep='')
    print('Across:')
    printout(across)         
    print('Down:')
    printout(down)
    print()
    count+=1
