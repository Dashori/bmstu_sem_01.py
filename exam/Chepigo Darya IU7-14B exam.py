##Даны 2 текстовых файла in1.txt и in2.txt, в которые записаны неубывающие последовательности натуральных чисел
##(по одному числу в строке, значения чисел не превышают 3000).
##Не используя списки и методы сортировки, а также не
##считывая файлы в память целиком, сформировать файл out.txt, в который записать
##неубывающую последовательность чисел, содержащую все числа из исходных файлов.
##Далее сформировать файл out1.txt, в который записать римские представления чисел из файла out.txt, выравненные по центру.
##Чепиго Дарья ИУ7-14Б

def rim(num):
    num=int(num)
    number=''
    nums={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    nums_list=['M','D','C','L','X','V','I']
    for i in nums_list:
        while num>=nums[i]:
            number+=i
            num-=nums[i]
    return number
        
f=open('in1.txt','r')
count_1=0  ##количество чисел в 1 файле
for i in f:
    count_1+=1
f.close()

count_2=0  ##количество чисел во 2 файле
g=open('in2.txt','r')
for i in g:
    count_2+=1
g.close()

##print(count_1,count_2)

f=open('in1.txt','r')
g=open('in2.txt','r')
h=open('out.txt','w')
f1=f.readline()
g1=g.readline()
i=j=0

##соединение файлов
while i<=(count_1-1) and j<=(count_1-1):
    if f1 and g1 and int(f1)<int(g1):
        h.write(f1)
        i+=1
        if i==count_1:
            break
        f1=f.readline()
    elif f1 and g1 and int(f1)==int(g1):
        h.write(f1)
        h.write(g1)
        i+=1
        j+=1
        if i==count_1 or j==count_2:
            break
        f1=f.readline()
        g1=g.readline()
    else:
        h.write(g1)
        j+=1
        if j==count_1:
            break
        g1=g.readline()

while i<=count_1-1:
    h.write(f1)
    i+=1
    f1=f.readline()
while j<=count_2-1:
    h.write(g1)
    j+=1
    g1=g.readline()

    
f.close()
g.close()
h.close()

h=open('out.txt','r')
k=open('out1.txt','w')

for i in h:
    i=rim(i)
    k.write('{:^10}'.format(i)+'\n')
h.close()
k.close()


