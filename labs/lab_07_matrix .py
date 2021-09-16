##Лабораторная работа №7
##Цель 1 работы: в квадратной матрицу размера меньше 7 определить все
##гласные буквы, которые в ней встречались ровно 1 раз
##записать их в одномерный массив в алфавитном порядке

vowels=list('aeiouy')             ##список гласных букв для проверки элементов
numbers=list('01234567')          ##список чисел для проверки элемента на int
numbers1=list('0123456789')          ##список чисел для проверки элемента на int


def vowel(x):                        ##функция для определения элемента
    z=0                              ##счетчик количества гласных 
    row=list(str(x))                 ##разбиение вставляемого элемента на список для проверки
    for i in range(len(row)):
        if row[i] in vowels:
            z=z+1
    if z!=0:
        z=1
    return(z)

def intovoe(x):
    row=list(str(x))
    count=0                             ##счетчик количества цифр в числе                
    for i in range(len(row)):
        if row[i] in numbers:
            count+=1
    if count==len(row):
        count=1
        x=int(x)
        if x>0 and x<7:
                count=1
        else:
                count=0
    else:
        count=0
    return(count)

def define(el):             ##функция для определения элемента
    el1=list(str(el))       ##разбиение вставляемого элемента на список для проверки
    minus=0                 ##есть ли минус
    point=0                 ##point-количество точек  элементе
    kol=0                   ##kol-количество цифр в элементе
    if el1[0]=='-':         ##проверка является ли элемент отрицаельным числом
        minus=1
    for i in range(len(el1)):
        if el1[i]=='.':               ##проверка является ли элемент числом  типа float
            point+=1    
        if el1[i] in numbers1:             ##подсчет количества цифр в элементе
            kol=kol+1
    if el1[0]!='.' or el1[len(el1)-1]!='.':
        point==2
    if point==1 and minus==1 and len(el1)==kol+2:      ##если число float отрицательное
        z=1
    elif point==1 and minus==0 and len(el1)==kol+1:    ##если число float положительное
        z=2
    elif point==0 and minus==0 and len(el1)==kol:      ##если число целое и положительное
        z=3
    elif point==0 and minus==1 and len(el1)==kol+1:    ##если число целое и отрицательное
        z=4
    else:                                              ##если это строка
        z=5
    return z

s=str(input('Введите количесство строчек и столбцов в квадратной матрице, от 1 до 7: '))
while intovoe(s)!=1:
    s=str(input('Введите натуральное число от 1 до 7: '))
s=int(s)
matrix=[]                            ##матрица
row_vowel=[]                         ##список для символов,которые содержат гласные
total=[]                             ##cписок гласных букв в алфавитном порядке

for i in range(s):
    matrix.append([0]*s)
for i in range(s):
    print('Введите через enter элементы',i+1,'строчки: ')
    for j in range(s):
        matrix[i][j]=str(input())
        if vowel(matrix[i][j])==1:
            row_vowel.append(matrix[i][j])
	    
row_vowel=''.join(row_vowel)                ##создание общей строчки со всеми элементами, содержащими гласные буквы
if row_vowel.count('a')==1:                 ##подсчет в этой строке количества гласных букв
    total.append('a')
if row_vowel.count('e')==1:
    total.append('e')
if row_vowel.count('i')==1:
    total.append('i')
if row_vowel.count('o')==1:
    total.append('o')
if row_vowel.count('u')==1:
    total.append('u')
if row_vowel.count('y')==1:
    total.append('y')
    
print()
print('Исходная матрица: ')
for i in matrix:
    for j in i:
    	print(j,end='  ')
    print()
print()

print('Список гласных букв, встречающихся один раз: ')
if len(total)!=0:
    for i in range(len(total)):
        print(total[i],end='    ')
else:
    print('В матрице нет гласных букв, встречающихся один раз')
print()

##Цель второй работы:в матрице (20,12) вычеркнуть строчку с наибольшем элементом
##Далее в каждой строке посчитать среднее арифметическое и аналогично посчитать кол-во 
##элементов,которые его превышают. Разместить это кол-во в массиве К.
    
print()
line=5
column=4
matrix=[]
k=[0]*(line-1)
for i in range(line):
    matrix.append([0]*column)
for i in range(line):
    print('Введите через enter элементы',i+1,'строчки: ')
    for j in range(column):
        matrix[i][j]=str(input())
        while define(matrix[i][j])==5:
            matrix[i][j]=str(input('Элемент должен быть числом, введите еще раз: '))
        matrix[i][j]=float(matrix[i][j])
        
maxim=matrix[0][0]                             ##максимальный элемент
maxi=0                                         ##строчка, в которой находится максимальный элемент
for i in range(line):
    for j in range(column):
        if matrix[i][j]>maxim:
            maxim=matrix[i][j]
            maxi=i
del matrix[maxi]                               ##удаление строчки с максимальным элементом

for i in range(line-1):                        ##добавление столбца, чтоб там хранить ср.арифм каждой строчки
    matrix[i].append(0)
    
for i in range(line-1):                        ##подсчет суммы каждой строки
    for j in range(column):
        matrix[i][column]+=matrix[i][j]
        
for i in range(line-1):                        ##подсчет среднего арифметического каждой строки
    matrix[i][column]=matrix[i][column]/column
    

for i in range(line-1):                        ##заполнение списка К с количеством элементов, превышающих ср арифм строки
    for j in range(column):
        if matrix[i][j]>matrix[i][column]:
            k[i]=k[i]+1
for i in range(line-1):
    del matrix[i][column]                      ##удаление доп столбца
    
print()    
print('Полученная матрица:')
print()

for i in range(line-1):
    for j in range(column):
    	print('{:^6.3g}'.format(matrix[i][j]),end='   ')
    print()

print('Список с количеством элементов, которые превышают среднее арифметическое')
for i in range(len(k)):    
    print(k[i],end='   ')

