##Цель программы: вычислить значение двух заданных функций на интервале,
##который вводит пользователь
##оформить это в виде таблицы,а также построить график одной из них
##Автор: Чепиго Дарья, ИУ7-14Б

from  math import e,cos,pi

n = float(input('Введите начало интервала: '))           ## Ввод начала интервала
shag = float(input('Введите шаг интервала: '))           ## Ввод шага интервала
k = float(input('Введите конец интервала: '))            ## Ввод конца интервала
mr=[]                        ##массив для сохранения значений, чтоб построить график 
mn=mx=0                      ##максимальное и минимальное значение функции
z = int((k - n) / shag)      ##подсчет количества входа в цикл for
a = n
l=0
print('   x      |      y                              |       y2             ')              ##создание таблицы
print('----------------------------------------------------------------------------') 

for i in range(z+1):                            ##цикл для вывода таблицы значений
    p = 0.471 * (e ** (-a)) * cos(pi * a * a)
    r = 0.21 - 2.52 * a + (a ** (3))
    mr.append(r)
    if i==0:                                    ##поиск минимума и максимума функции
        mx=mn=r
    elif r>mx:
        mx=r
    elif r<mn:
        mn=r
    print('{:7.2f}    |   {:<32.3g} |     {:<20.3g}   '.format(a, p, r))
    a = a + shag

kol=int(input('Введите количество засечек от 4 до 8: '))
x=abs(mx-mn)                 ##максимальный разбег функции 
raz=x/(kol-1)   
zz=int((150-kol)/(kol-1))    ##вычисление количества пробелов между засечками
print('   ','{:^10.3g}'.format(mn),end='')
mn1=mn+raz

for i in range(kol-1):  
    print(' '*(zz-11),'{:^10.3g}'.format(round(mn1,1)),end='')
    mn1+=raz
print(' ')

print('        ',end='')
for i in range (150):  ## вывод оси У
    if i%zz!=0:
        print('-',end='')
    else:
        print('|',end='')
print('----> Y')
p=2
if mn*mx<0:       ##проверка проходит ли функция через ось игрик
    p=1                         ##да, так как меняет знак
elif mn*mx==0:    ##один из крайних элементов и есть ноль, иначе
    p=0
zz=int((150-kol)/(kol-1))
zz=zz*(kol-1)+1
k0=int(abs((zz*mn)/x)) ## там где ось Х, если она есть
for j in range(z+1):  
    if mr[j] <= 0 :
         r = (mr[j]-mn)*(zz)/x
         r = int(r)
    elif mr[j] > 0:
         r = ((abs(mn)+mr[j])*(zz))/x
         r = int(r)
    if p==2:  ##случай, когда ось икс отсутвует
        r= ((mr[j]-mn)*zz)/x
        r=int(r)
        print('{:^8.1f}'.format(n),' '*(r),'*', sep='') 
    if p==1 or p==0:  ##случай, когда ось икс посреди графика
        if r>k0:
            print('{:^8.1f}'.format(n),' '*(k0),'|',' '*(r-k0-1),'*', sep='')
        elif k0>r:
            print('{:^8.1f}'.format(n),' '*(r),'*',' '*(k0-r-1),'|', sep='')
        elif r==k0:
            print('{:^8.1f}'.format(n),' '*(k0),'*', sep='')
    n=n+shag
if p==1 or p==0:
    print(' '*(7+k0),'|')
    print(' '*(7+k0),'V X')
