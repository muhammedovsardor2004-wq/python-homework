import string

num = int(input("Har bir qatorda nechta harf bo‘lsin? "))

alphabet = string.ascii_uppercase

with open('letters.txt', 'w') as f:
    for i in range(0, len(alphabet), num):
        f.write(" ".join(alphabet[i:i+num]) + "\n")

try:
    age = input("Yoshingizni kiriting: ")

    if not age.isdigit():      
        raise ValueError("Janob, butun son kiriting!")  

    age = int(age)
    print(f"Sizning yoshingiz: {age}")

except ValueError as e:
    print(e)


try:
    f = open("rasm.jpg", "r")  
    matn = f.read()
    print(matn)

except FileNotFoundError:
    print("Janob, fayl topilmadi.")


try:
    a = input('1 - sonni kirit')
    b = input('2 - sonni kirit')

    if not a.isdigit() or not b.isdigit():
        raise ('son kirit')
    
    a = int(a)
    b = int(b)

    total = a+b
    print(total)

except TypeError as t:
    print(t)




try:
    with open("protected_file.txt", "w") as f:  
        f.write("Salom, Janob!")

except PermissionError:
    print("Janob, bu faylga yozishga ruxsatingiz yo‘q.")


try:
    index = int(input('index kirit'))
    my_list = [1,2,3,4,'bir']
    print(my_list[index])
except IndexError:
    print('bunday index yuq')
except ValueError:
    print("Janob, index sifatida faqat son kiriting.")


try:
    num = int(input('son kirit'))
    print(num)
except KeyboardInterrupt:
    print('bekor qilindi')

try:
    num = int(input('son kirit'))
    division = 10 / num
    print(division)
except ArithmeticError:
    print('matematik xato ')


try:
    with open("my_file.txt", "r", encoding="ascii") as f:
     matn = f.read()
    print(matn)
except UnicodeDecodeError:
   print('chota neto')



try:
    name = 'sardor'
    total = name.append('bek')
    print(total)
except AttributeError:
    print('bunaqa funksiya yuq')

with open("my_file.txt", 'r') as f:
    fole= f.read()
    print(fole)


son = int(input('nechta qator o`isin'))

with open('my_file.txt','r') as f:
    for i in range(1,son+1):
        print(f.readline())



with open('my_file.txt','a') as f:
    yangi = f.write('yaxshi\n')
    print(yangi)

with open('my_file.txt','r') as d:
    file = d.read()
    print(file)



n = int(input('soni kirit'))

with open('my_file.txt','r') as f:
    file = f.readlines()

    oxirgilar = file[-n:]
    for i in oxirgilar:
        print(i,end='')


lines = []
with open('my_file.txt','r') as f:
    for line in f:
        lines.append(line)

print(lines)


totals = []

with open('my_file.txt','r') as f:
    for line in f:
        totals.append(line)

print(totals)



lists = []

with open('my_file.txt','r') as f:
    for line in f:
        lists.append(line)

print(lists)


with open('my_file.txt','r') as f:
    words = f.read().split()

    max_num = max(len(i)  for i in words)

    max_word = [i for i in words if len(i) == max_num]


print(max_word)



with open('my_file.txt','r') as f:
    count = sum(1 for _ in f)

print('qatorlar soni:',count, 'ta')


from collections import Counter

with open('my_file.txt','r') as f:
    file = f.read().split()

count = Counter(file)

print(count)


import os

file_size = os.path.getsize('my_file.txt')

print(file_size)


my_list = [1,3,4,'nima gap','sardor']

with open('my_file2.txt','w') as f:
    for i in my_list:
        f.write(str(i) + '\n')


with open('my_file2.txt','r') as f:
    with open('new_file.txt',"w") as n:

        n.write(f.read())


with open('my_file2.txt','r') as f1, open('new_file.txt' ,'r') as f2:
    for line1, line2 in zip(f1,f2):
        print(line1.strip(), '+' ,line2.strip())


import random

with open('my_file.txt', 'r') as f:
    file = f.readlines()

    random_chois = random.choice(file)

print(random_chois)


f = open('my_file.txt', 'r')

print('Fay; yopilganmi:',f.closed)

f.close()

print('Fayl yopilganmi:',f.closed)



with open('my_file.txt','r') as f:
    file = f.read().replace('\n','')

with open('new_file.txt','w') as n:
    n.write(file)

with open('new_file.txt','r') as ff:
    new_file = ff.read()

print(new_file)



with open('num_file.txt','w') as f:
    file = f.write('hammasi,yaxshimi,nima,gap')

with open('num_file.txt','r') as f:
    alohida = f.read().replace(',',' ').split()
    jami = len(alohida)

print(jami)



files = ['num_file.txt','my_file2.txt']

total = []

for filename in files:
    with open(filename,'r') as f:
        words = f.read()
        for ch in words:
            total.append(ch)

print(total)




import string

for filename in string.ascii_uppercase:
    with open(filename,'w') as f:
        file = f.write('Sardor')



import string

num = int(input("Har bir qatorda nechta harf bo‘lsin? "))

alphabet = string.ascii_uppercase

with open('letters.txt', 'w') as f:
    for i in range(0, len(alphabet), num):
        f.write(" ".join(alphabet[i:i+num]) + "\n")


