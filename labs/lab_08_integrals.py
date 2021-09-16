##Лабораторная работа №8
##Используя метод Уэддля и метод срединных прямоугольников
##найти определенный интеграл на интервале, используя 2 количества разбиений.

f = 0                        ##Переменная для функции, для которой берется интеграл
def func(x):                 ##Функция для функции
    f = (x)
    return(f)

def proto(a,b):
    proto_1=((b^2)-(a^2))/2
    return(proto_1)

def define(el):          ##функция для определения элемента
    numbers=list('0213456789')
    el_1=list(str(el))    ##разбиение вставляемого элемента на список для проверки
    minus=0              ##есть ли минус
    point=0              ##point-количество точек  элементе
    kol=0                ##kol-количество цифр в элементе
    if el_1[0]=='-':      ##проверка является ли элемент отрицаельным числом
        minus=1
    for i in range(len(el_1)):
        if el_1[i]=='.':               ##проверка является ли элемент числом  типа float
            point+=1    
        if el_1[i] in numbers:             ##подсчет количества цифр в элементе
            kol=kol+1
    if el_1[0]!='.' or el_1[len(el_1)-1]!='.':
        point==2
    if point==1 and minus==1 and len(el_1)==kol+2:      ##если число float отрицательное
        z=1
    elif point==1 and minus==0 and len(el_1)==kol+1:    ##если число float положительное
        z=2
    elif point==0 and minus==0 and len(el_1)==kol:      ##если число целое и положительное
        z=3
    elif point==0 and minus==1 and len(el_1)==kol+1:    ##если число целое и отрицательное
        z=4
    else:                                              ##если это строка
        z=5
    return z

def inlet(el):                                   ##функция для повторного ввода в случае ошибки
    while define(el)==5:
        el=str(input('Введите еще раз элемент-число: '))
    if define(el)<=2:
        el=float(el)
    elif define(el)<=4:
        el=int(el)
    return(el)
def int_inlet(el):                               ##функция для повторного ввода чисел int
    while define(el)!=3:
        el=str(input('Введите еще раз элемент-целое положительное число: '))
    el=int(el)
    return(el)


def rect(n,a,b):     ##Метод срединных прямоугольников
    rect1 = 0
    h1 = abs((b-a)) / n   ##шаг
    for i in range(n + 1):  
        rect1 = rect1 + func(a - (h1 / 2) + i * h1) 
    rect1 = abs(rect1 * h1)
    return(rect1)

def weddle(n,a,b):                         ##Метод Уэддля
    odd = (3 / 10,15 / 10,3 / 10,18 / 10,3 / 10,15 / 10,3 / 10)  ##коэффициенты для метода Уэддля
    weddle1 = 0
    h1 = abs((b-a)) / n  ##шаг
    z1 = h1 / 6                 ##коэффициент
    for i in range(n + 1):
        weddle1+=odd[0] * func(a + i * h1 - 6 * z1) + odd[1] * func(a + i * h1 - 5 * z1)\
        +odd[2] * func(a + i * h1 - 4 * z1) + odd[3] * func(a + i * h1 - 3 * z1)\
        +odd[4] * func(a + i * h1 - 2 * z1)+ odd[5] * func(a + i * h1 - z1) + odd[6] * func(a + i * h1)
    weddle1 = abs(weddle1 * z1)
    return(weddle1)


start = str(input('Введите начало интервала: '))
start=inlet(start)

end = str(input('Введите конец интервала: '))
end=inlet(end)

eps = str(input('Введите точность eps: '))
eps=inlet(eps)

n1 = str(input('Введите первое количество разбиений: '))
n1=int_inlet(n1)

n2 = str(input('Введите второе количество разбиений: '))
n2=int_inlet(n2)

print('Метод',' ' * 25,'|    N1 =',n1,' ' * 6,'  |      N2 =',n2)
print('-' * 70)
print('Метод срединных прямоугольников |','{:^10.3f}'.format(rect(n1,start,end)),
      '        |','{:^10.3f}'.format(rect(n2,start,end)))
print('Метод Уэддля                    |','{:^10.3f}'.format(weddle(n1,start,end)),
      '        |', '{:^10.3f}'.format(weddle(n2,start,end)))
print(' ')

##замена переменных, чтоб посчитать погрешности и интеграл с точностью
k1,k2 = n1,n2 
k3 = 2 * k1
k4 = 2 * k2

weddle_eps = 0    ##переменная для вычисления интеграла с точностью и шагом n1
weddle_eps2 = 0   ##переменная для вычисления интеграла с точностью и шагом n2
while abs(weddle(k3,start,end) - (weddle(k1,start,end))) > eps:
       weddle_eps = weddle(k3,start,end)
       k1,k3 = k3,k3 * 2
while abs(weddle(k4,start,end) - (weddle(k2,start,end))) > eps:
       weddle_eps2 = weddle(k4,start,end)
       k2,k4 = k4,k4 * 2
       
print('Метод Уэддля с точностью','{:^5.3g}'.format(eps),
      'для количества разбиений',n1,'равен = ','{:<10.5f}'.format(weddle_eps))
print('Метод Уэддля с точностью','{:^5.3g}'.format(eps),
      'для количества разбиений',n2,'равен = ','{:<10.5f}'.format(weddle_eps2))
print('')

mistake_abs = abs(proto(start,end) - weddle(n1,start,end))    ##Aбсолютная ошибка
print('Абсолютная ошибка при методе Уэддля для',n1,
      'разбиений =','{:<10.3g}'.format(mistake_abs))
mistake_rel = mistake_abs / abs(weddle(n1,start,end))   ##Относительная ошибка
print('Относительная ошибка при методе Уэддля для',n1,
      'разбиений =','{:<10.3g}'.format(mistake_rel))


