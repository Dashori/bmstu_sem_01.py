##Лабораторная работа №10
##Автор: Чепиго Дарья
##Задан текст массивом строк. Текст - фрагмент литературного произведения (5-7
##предложений). Ни одна строка не оканчивается точкой кроме последней.
##Текст задается в программе, пользовательский ввод не требуется.
##Необходимо создать меню, выполняющее следующие действия:
print('''Пункты меню:
1. Выравнивание текста по левому краю.
2. Выравнивание текста по правому краю.
3. Выравнивание текста по ширине.
4. Удаление заданного слова.
5. Замена одного слова другим во всем тексте.
6. Вычисление арифметического выражения.
7. Найти наиболее часто встречающееся слово в каждом предложении
''')

circle=0
##список символов, которые могут встречаться рядом со словами
mark = ['.',',',':',';','-','=']
##список символов, которые заканчивают предложение
end=['.','!','?']
##cписок возможных мат операций
math=['^','*','/','+','-']
##cписок цифр
numbers='0123456789'
brackets='()'
##cписок возможных пунктов меню
menu_num='1234567'
##символы, из которых могут состоять слова
alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'

text=['Вы помните? 3*15+6/6*6 вы всё, конечно, помните!',
'Как я стоял, 7^(1+1)*7/7-65 привет приблизившись  к стене',
'Взволованно 2^2^2^2/256 ходили вы по комнате',
'И что-то резкое лицо бросали мнe',
'  яблоко яблоков яблок                         ',

'Вы говорили: 1-3*5 нам пора расстаться,',
'Что вас измучила моя шальная жизнь, что вам пора за дело приниматься',
'А мой удел  катиться дальше, вниз, вниз.',
'Ноябрь (((19*1*10*10)+48/2)).']

print('Исходный текст: \n')
for i in range(len(text)):
    print(text[i])
print()

def space(text_1):      ##Функция для удаления лишних пробелов между словами+right
    new_text = [0]*len(text_1)
    for i in range(len(text_1)):   
        j = text_1[i].split()##разделение всех слов 
        new_text[i] = ' '.join(j) ##вставка между ними одного пробела
    return(new_text)

def width(text_1):           ##функция для нахождения самой длинной строки
    max_len=0
    for i in range(len(text_1)):
        if len(text_1[i])>max_len:
            max_len=len(text_1[i])
    return(max_len)        ##запоминаем длину самой длинной строки

def left(text_1):         ##функция для выравнивания по левому краю
    text_1=space(text_1)
    for i in range(len(text_1)):
        r=' '*(width(text_1)-len(text_1[i]))
        text_1[i]=r+text_1[i]
    return(text_1)

def count(text_1):       #функция для подсчета количества слов в каждой строке текста
    text_1=space(text_1)
    count_1=[0]*len(text_1)
    for i in range(len(text_1)):
        j=text_1[i].split()
        for k in range(len(j)):
            if j[k] not in mark:
                count_1[i]+=1
    return(count_1)

def middle(text_1):      ##функция для выравнивания по ширине
    text_1=space(text_1)
    max_len=width(text_1)
    for i in range(len(text_1)):
        if max_len > len(text_1[i]):
            strt =''
            c_probel = 0 ##счетчик количества пробелов в строке
            for j in range(len(text_1[i])):
                if text_1[i][j]==' ':
                    c_probel += 1
            # Добавление пробелом между словами, в зависимости от длины строки           
            probel = [0]*c_probel
            delta = max_len - len(text_1[i]) ##количество пробелов, которые надо добавить в строку
            if c_probel!=0:
                k1 = delta // c_probel
            else:
                k1=0
            for j in range(c_probel):
                probel[j] = k1+1
            if c_probel!=0:
                k1 = delta%c_probel
            else:
                k1=0
            k = 0
            while k1>0:
                probel[k] += 1
                k1 -= 1
                k += 1
            # Форматированный вывод текста    
            k = 0    
            for j in range(len(text_1[i])):
                if text[i][j]!=' ':
                    strt += text_1[i][j]
                else:
                    strt += ' '*probel[k]
                    k += 1
            print(strt)
        else:
            print(text_1[i])
    print()
    
def mark1(a):   ##функция чтоб проверять слово без последнего эелемента
    u=a         ##так как он может является знаком препинания
    u=u.lower()
    for i in range(len(a)):
        if a[i] in mark:
            u=a[:(len(a)-1)]   
    return(u)

def word(a):   ##функция для определения слово это или нет
    t=1
    for i in range(len(a)):
        if a[i] not in alphabet:
            t=0
            break
    return(t)
def number(a):  ##функция для определения является ли элемент числом
    a1=list(str(a))
    k=0
    for i in range(len(a1)):
        if a1[i] in numbers:
            k=k+1
    if k==len(a1):
        k=1   ##это число
    else:
        k=0   ##это не число
    return(k)

def prior(a):  ##функция для определения приоритетов выражений
    pr=0
    if a=='(':
        pr=0
    elif a=='+' or a=='-':
        pr=1
    elif a=='*' or a=='/':
        pr=2
    elif a=='^':
        pr=3
    return(pr)

def empty(a):
    if len(a)>0:
        k=1 ##стэк не пустой
    else:
        k=0 ##стэк пустой
    return(k)

def stack2(a):  ##создание очереди при вычислении арифм. выражений
    stack1=[]   ##в польской нотации
    line1=[]
    for i in range(len(a)):
        if number(a[i])==1 : ##если число- в исходную строку
            line1.append(a[i])
        elif a[i] in math: ##если мат символ, то проверяем
            if empty(stack1)==0 or prior(stack1[len(stack1)-1])<prior(a[i]):
                ##если стэк пустой-помещаем туда
                stack1.append(a[i])
##                print(stack1)

            elif empty(stack1)==1:  #если посл элемент имеет больший приоритет
               for w in range(len(stack1)-1,-1,-1):
                   if prior(stack1[len(stack1)-1])>=prior(a[i]):
##                   for w in range(len(stack1)-1,-1,-1):
##                        for k in range(w,-1,-1):     
                        line1.append(stack1[w])
                        del stack1[w]
               if empty(stack1)==0 or prior(stack1[len(stack1)-1])<prior(a[i]): 
                    stack1.append(a[i])
                    
        elif a[i]=='(':
            stack1.append(a[i])
        elif a[i]==')':
            l=len(stack1)-1
            if l>=0:
                while l>-1 and  stack1[l]!='(' :
                    line1.append(stack1[l])
                    del stack1[l]
                    l=l-1
                if l>=0:    
                    while l>0 and stack1[1]=='(':
                        del stack1[l]
                        l=l-1
                    if l==0 and stack1[l]=='(':
                        del stack1[l]
                    
    if len(stack1)>0:
        for i in range(len(stack1)-1,-1,-1):
            line1.append(stack1[i])
            del stack1[i]
##    print(line1)        
    return(line1)

def stack3(a2):  ##подсчет в польской нотации
    line2=[]
    n1=n2=res=0
    for i in range(len(a2)):
        if number(a2[i])==1:
            a2[i]=int(a2[i])
            line2.append(int(a2[i]))   
        k=len(line2)-1
        if a2[i] in math and k>0:
            if a2[i]=='+':
                line2[k-1]+=line2[k]
                line2.pop(k)
            elif a2[i]=='-':
                line2[k-1]-=line2[k]
                line2.pop(k)
            elif a2[i]=='*':
                line2[k-1]=line2[k-1]*line2[k]
                line2.pop(k)      
            elif a2[i]=='/':
                line2[k-1]/=line2[k]
                line2.pop(k)
            elif a2[i]=='^':
                line2[k-1]=line2[k-1]**(line2[k])
                line2.pop(k)
    return(line2[0]
           )
def num(t):   ##функция чтоб объединять цифры
    t1=[]
    t2=[]
    for i in range(len(t)):
        if t[i] in numbers:
            t1.append(t[i])
        else:
            t3=''.join(str(x) for x in t1)
            t2.append(t3)
            t2.append(t[i])
            t1=[]
            t3=0
    o=len(t)-1
    if o>-1:
        t3=''.join(str(x) for x in t1)
        t2.append(t3)
    for i in range(len(t2)-1,-1,-1):
        if t2[i]=='':
            del t2[i] 
    return(t2)       
        
alignment=0  ##переменная чтобы запоминать выравнивание

while circle!=1:
    menu=str(input('Выберите пункт меню: '))
    print('')
    while menu not in menu_num:
        menu=str(input('''Пунктом меню является число от 1 до 7.
Введите еще раз: '''))
        print('')
    if menu=='1':
        text=space(text)
        for i in range(len(text)):
            print(text[i])
        print()
        alignment=1
    if menu=='2':
        text=left(text)
        for i in range(len(text)):
            print(text[i])
        print()
        alignment=2
    if menu=='3':
        text=space(text)
        middle(text)
        alignment=3
        
    if menu=='4':
        text_del = [0]*len(text)
        delete=str(input('Введите слово, которое надо удалить: '))
        delete=delete.lower()
        while word(delete)!=1:
            delete=str(input('Удалемый элемент- слово, введите еще раз: '))
            delete=delete.lower()       
        for i in range(len(text)):
            j=text[i].split()
            for k in range(len(j)):
                low=j[k].lower()
                low_mark=mark1(low)
                if j[k]==delete or low==delete or low_mark==delete:
                   j[k]=''
            text_del[i] = ' '.join(j)
        text=text_del
        text=space(text)
        if alignment==2:
            text=left(text)
        if alignment==3:
            middle(text)
        if alignment!=3:
            for i in range(len(text)):
                print(text[i])
            print()
        
    if menu=='5':
        replace=str(input('Введите слово, которое надо заменить: '))
        while word(replace)!=1:
            replace=str(input('Заменяемый элемент- слово, введите еще раз: '))
            replace=replace.lower()
        swap=str(input('Введите вставляемое слово: '))
        while word(swap)!=1:
            swap=str(input('Вставляемый элемент- слово, введите еще раз: '))
            swap=swap.lower()
        text_rep = [0]*len(text)
        for i in range(len(text)):
            j=text[i].split()
            for k in range(len(j)):
                low=j[k].lower()
                low_mark=mark1(low)
                if j[k]==replace or low==replace or low_mark==replace:
                    j[k]=swap
            text_rep[i]=' '.join(j)
        text=text_rep
        text=space(text)
        if alignment==2:
            text=left(text)
        if alignment==3:
            middle(text)
        if alignment!=3:
            for i in range(len(text)):
                print(text[i])
            print()
               
    if menu=='7':  ##Найти наиболее часто встречающееся слово в каждом предложении
        text=space(text)
        long=[0]*len(text)
        line=[]
        poem=[]
        point=0 ##счетчик количества точек, т.е. предложений
        poem=' '.join(i for i in text) ##переписывание всего стиха в один список
        for i in poem:  ##подсчет количества предложений в тексте
            if i in end:
                point+=1
        sent=[]  ##разбиение текста по предложениям
        sent_1=[] ##разбиение предложения по словам
        k=0
        for l in range(point):
            sent.append([])
            sent_1.append([])
        for i in poem:
            if i not in end:
                sent[k]+=' '.join(i)
            else:
                sent[k]+=' '.join(i)
                k=k+1
                if k==point:
                    break
        for i in range(point): ##разбиение текста по предложениям       
            sent_1[i]=''.join(x for x in sent[i])
##            print(sent_1[i])
            
        for i in range(point): ##разбиение предложения по словам
            sent_1[i]=sent_1[i].split()
        
        ##все повтор слова в предложении записывем в массив
        slov=[]
        for i in range(point):
            slov.append([])
        for i in range(point):
            for j in range(len(sent_1[i])):
                for k in range(j):
                    if mark1(sent_1[i][j])==mark1(sent_1[i][k]):
                        slov[i].append(mark1(sent_1[i][j]))
##        print('slow',slov)
        slov_1=[]
        for i in range(len(slov)):
            slov_1=[]
            for j in range(len(slov[i])):
                slov_1.append(1)
            for j in range(len(slov[i])):
                for k in range(j-1):
                    if slov[i][j]==slov[i][k]:
                        slov_1[k]+=1
##            print(slov_1)            
            if len(slov_1)>0:
                max_sl=slov_1[0]
                index=0
                for p in range(1,len(slov_1)):
##                    print(slov_1[p])
                    if slov_1[p] >max_sl:
                        max_sl=slov_1[p]
                        index=p
                print('В предложении номер ',i+1,'самое популярное слово: ',slov[i][index])
        print()       
    if menu=='6':
        term=[] ##Список для мат выражений в каждой строчке
        for i in range(len(text)):
            term.append([])
            
        for i in range(len(text)): ##В каждой строчке находим математическое выражение
            for j in range(len(text[i])):
                if text[i][j] in numbers or text[i][j] in math or text[i][j] in brackets:
                    term[i].append(text[i][j])
                    
        for i in range(len(term)):
            term[i]=num(term[i]) ##объединяем список по числам
            
        for i in range(len(term)):
            if len(term[i])>=2:
                k=''.join(str(x) for x in term[i])
                term[i]=stack2(term[i])     ##Перевод в польскую нотацию
##                print(term[i])
                if len(term[i])>=2:
                    term[i]=stack3(term[i]) ##Подсчет в польской нотации
                    print(k,' = ',term[i])
                   
        
