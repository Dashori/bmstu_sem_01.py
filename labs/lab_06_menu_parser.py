##Лабораторная работа №6
##Цель программы: меню,состоящее из 7 пунктов
##Необходимо проверять все входные данные на соответствие условиям
##Автор- Чепиго Дарья ИУ7-14Б
print('''Пункты меню:
1.Проинициализировать список первыми N элементами заданного ряда
2.Добавить элемент в произвольное место списка
3.Удалить произвольный элемент из списка
4.Очистить список
5.Найти значение K-го экстремума в списке, если он является списком чисел
6.Найти наиболее длинную убывающую последовательность отрицательных чисел,модуль которых-простое число 
7.Найти наибольшую последовательность строк, содержащих только гласные буквы
''')

circle=1                      ##переменная для бесконечного вхождения в цикл
numbers_1=list('1234567890')  ##список чисел
vowel=list('ayuioe')          ##список гласных букв
numbers_2=list('1234567')     ##список цифр для меня
ext=[]                        ##список для экстремумов

def define(el):             ##функция для определения элемента
    el1=list(str(el))    ##разбиение вставляемого элемента на список для проверки
    minus=0              ##есть ли минус
    point=0              ##point-количество точек  элементе
    kol=0                ##kol-количество цифр в элементе
    if el1[0]=='-':      ##проверка является ли элемент отрицаельным числом
        minus=1
    for i in range(len(el1)):
        if el1[i]=='.':               ##проверка является ли элемент числом  типа float
            point+=1    
        if el1[i] in numbers_1:             ##подсчет количества цифр в элементе
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

def simple(a):                ##функция для определения простое ли число 
    d=0                        ##cчетчик количества делителей
    if define(a)!=5:
        for i in range(1,int(abs(a)/2)+1):
            if abs(a)%i==0:
                d=d+1
    return d

def vowel(a):                ##функция для определения гласная ли буква
    a=list(str(a))
    g=0                      ##если g=1- буква гласная
    for i in range(len(a)):
        if a[i] in vowel:
            g=g+1
    if g==len(a):
        g=1
    else:
        g=0
    return(g)

def conc(m):                                      ##функция для вывода списка
    i=0
    for i in range(n):
        if define(m[i])!=5 or type(m[i])!=str:
            print('{:10.3g}'.format(m[i]), end=' ')
            i=i+1
        else:
            print('   ',m[i],end=' ')
            i=i+1
    print(' ')
while circle!=0:
    print(' ')
    num=str(input('Введите номер выбранного пункта: '))
    if num in numbers_2:
        num=int(num)
        if num==1:
            n=str(input('Введите количество элементов в списке: '))
            while define(n)!=3:
                n=str(input('Введите количество элементов в списке-целое положительное число: '))
            n=int(n)
            x=str(input('Введите X для заданного ряда: '))
            while define(x)==5:
                x=str(input('Введите X для заданного ряда-число: '))
            x=float(x)
            m=[0]*n             ##список
            if n!=0:
                m[0]=t=1        ##t-переменная для чередования знака,m[0] всегда равен 1
            w=x        
            k=2             ##численный множитель элемента
            for i in range (1,n):
                w=w*x       ##степень Х
                t=t*(-1)    ##знак элемента
                m[i]=k*t*w  ##элемент
                k+=1        ##численный множитель для следующего элемента
            print('\n','Список после выполнения пункта 1')    
            for i in range(n):
                print('{:10.3g}'.format(m[i]),end=' ')
            print(' ')
            
        if num==2:
            el=str(input('Введите вставляемый элемент: '))
            place=str(input('Введите место для вставляемого элемента : '))
            while define(place)!=(3):
                    print('Число должно быть целым неотрицательным в промежутке от 0 до ',n)
                    place=str(input('Введите еще раз: '))
            while (int(place)>n or int(place)<0):
                print('Число должно быть в промежутке от 0 до ',n)
                place=str(input('Введите еще раз: '))
            place=int(place)
            if define(el)!=5:
                el=float(el)
            m.insert(place,el)
            n=n+1                 ##расширение списка
            print('\n','Список после выполнения пункта 2:')
            conc(m)
        
        if num==3:
            if n!=0:
                place=str(input('Введите номер удаляемого элемента : '))
                while define(place)!=(3):
                    print('Число должно быть целым неотрицательным в промежутке от 0 до ',n)
                    place=str(input('Введите еще раз: '))
                while (int(place)>n-1 or int(place)<0):
                    print('Число должно быть в промежутке от 0 до ',n-1)
                    place=str(input('Введите еще раз: '))
                place=int(place)
                for i in range(place,n-1):  
                    m[i]=m[i+1]          
                n=n-1                              ##изменение размера списка для вывода
                print('\n','Список после выполнения пункта 3:')
                conc(m)
            if n==0:
                print('Список пуст')
        
        if num==4:        
            m.clear()               ##очистка списка
            print('\n','Список после выполнения пункта 4:')
            print(m)
            
        if num==5:
            for i in range(n):
                if define(m[i])==5:
                    print('\n','Список не является списком чисел')
                    break
            else:
                k=str(input('Введите номер экстремума: '))
                if define(k)==3 and (int(k)<n-1):
                    k=int(k)
                    for i in range(1,n-1):
                        if (m[i-1]<m[i] and m[i]>m[i+1]) or (m[i-1]>m[i] and m[i]<m[i+1]):
                            ext.append(m[i])
                    if k<=len(ext):
                        print('Искомый экстремум: ','{:5.3g}'.format(ext[k-1]))
                    else:
                        print('В списке всего',len(ext),'экстремумов')
                else:
                    print('\n','Номер должен быть целым положительным числом и меньше',n-2)
                    
        if num==6:
            row1=[]            ##список для нахождения самой длинной последовательности
            row=[]             ##список для сохранения последовательностей во время поиска
            i=k=k1=0           ##k1-подсчет количества элементов в списке row1,k-в row соответсвено 
            for i in range(n-1):
                if define(m[i])!=5 and define(m[i+1])!=5:                        ##проверка что это числа
                    if m[i]<0 and m[i+1]<0 and m[i]>m[i+1] and (simple(m[i])==1) and (simple(m[i+1])==1) :    ##проверка что они меньше нуля и простые
                        row.append(m[i])
                        k=k+1
                    elif k>k1:
                        row.append(m[i])
                        k=k+1
                        row1=row
                        k1=k
                        row=[]
                        k=0
                    elif k<k1:
                        row=[]
                        k=0
                        
            if k==0 and k1==0:
                for i in range(n):
                    if (simple(m[i])==1) and define(m[i])!=5:
                        row.append(m[i])
                        k=k+1
                        break
            elif define(m[i+1])!=5 and simple(m[i+1])==1:
                row.append(m[i+1])
                k=k+1
            print('Искомая последовательность пункта 6 :')
            if k1>=k and (k1!=0 or k!=0):
                i=0
                for i in range(len(row1)):
                    print('{:4.3g}'.format(row1[i]),end=' ')  
            elif k1<k:
                i=0
                for i in range(len(row)):
                    print('{:4.3g}'.format(row[i]),end=' ')
            else:
                print('Искомая последовательноссть не существует')
              
        if num==7:
            row1=[]            ##список для нахождения самой длинной последовательности
            row=[]             ##список для сохранения последовательностей во время поиска
            i=k=k1=0            ##k1-подсчет количества элементов в списке row1,k-в row соответсвено
            for i in range(n-1):
                if define(m[i])==5 and define(m[i+1]==5):       ##проверка что это числа
                    if vowel(m[i])==1 and vowel(m[i+1])==1:   ##проверка что это гласные
                        row.append(m[i])
                        k=k+1
                    elif k>k1:
                        row.append(m[i])
                        k=k+1
                        row1=row
                        k1=k
                        row=[]
                        k=0
                    elif k<k1:
                        row=[]
                        k=0
            if k==0 and k1==0:
                for i in range(len(m)):
                    if define(m[i])==5 and define(m[i+1]==5): 
                        if vowel(m[i])==1:
                            row.append(m[i])
                            k=k+1
                            break
            else:
                row.append(m[i+1])
                k=k+1
            print('Искомая последовательность пункта 7:')
            if k1>=k and (k1!=0 or k!=0):
                for i in range(len(row1)):
                    print(row1[i],end=' ')  
            elif k1<k:
                for i in range(len(row)):
                    print(row[i],end=' ')
            else:
                print('Искомая последовательноссть не существует')

          
