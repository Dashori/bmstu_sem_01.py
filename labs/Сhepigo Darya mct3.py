## Исходный файл называется "in.txt" и никак иначе. 
##Используя редактор, создать текстовый файл in.txt. 
##В исходном файле записан текст -- отрывок литературного произведения.
##Текст содержит 5-7 предложений, записан в 5-7 строк файла так, что ни одна строка кроме последней не оканчивается точкой.
##Написать программу, создающую текстовый файл out.txt, в котором
##в первой строке записывается самое короткое предложение текста. Во второй строке -- самое длинное предложение.
##Затем измененный текст исходного файла, где после каждого предложения в скобках указывается количество слов в предложении.

mark=['!','?','.'] ##конец предложения
mark_1=['-',':'] ##символы в предложении
f=open('in.txt','r')
g=open('out.txt','w')
count=0
max_len=0
min_len=50
max_word=[]
min_word=[]
word=[]

for l in f:   ##считаем количество слов в предложении
    l=l.split() 
    for i in range(len(l)):
        if l[i][len(l[i])-1] not in mark:
            count=count+1
        elif l[i][len(l[i])-1] in mark:
            count=count+1
            l[i]=l[i]+'('+str(count)+')' 
            if count>max_len:
                max_len=count
            elif count<min_len:
                min_len=count
            count=0
            
##    st=' '.join(str(x) for x in l)
##    g.write(st+'\n')
##print(min_len)
##print(max_len)

count=0
f.close()
f=open('in.txt','r')
for l in f:  ##вывод минимальной
    l=l.split()
    for i in range(len(l)):
        if l[i][len(l[i])-1] not in mark:
            word.append(l[i])
            count+=1
        elif l[i][len(l[i])-1] in mark:
            count=count+1
            word.append(l[i])
            if count==min_len:    
                st=' '.join(str(x) for x in word)
                g.write(st+'('+str(count)+')'+'\n')
                break
            word=[]
            count=0
f.close()

f=open('in.txt','r')
for l in f: ##вывод максимальной
    l=l.split()
    for i in range(len(l)):
        if l[i][len(l[i])-1] not in mark:
            word.append(l[i])
            count+=1
        elif l[i][len(l[i])-1] in mark:
            count=count+1
            word.append(l[i])
            if count==max_len:    
                st=' '.join(str(x) for x in word)
                g.write(st+'('+str(count)+')'+'\n')
            word=[]
            count=0
f.close()
f=open('in.txt','r')

for l in f: ##вывод всех строк
    l=l.split() 
    for i in range(len(l)):
        if l[i][len(l[i])-1] not in mark:
            count=count+1
        if l[i] in mark_1:
            count=count-1
        elif l[i][len(l[i])-1] in mark:
            count=count+1
            l[i]=l[i]+'('+str(count)+')' 
            if count>max_len:
                max_len=count
            elif count<min_len:
                min_len=count
            count=0    
    st=' '.join(str(x) for x in l)
    g.write(st+'\n')
            
f.close()
g.close()
