1)
txt =  "abcdeighiafdvabfaabrebrro"

result = ''
vowels = 'aeiouAEIOU'
count  = 0

i = 0

while i < len(txt):
    result += txt[i]
    count += 1
    
    if count == 3:
        if txt[i] in vowels:
            if i + 1 < len(txt):
                result += txt[i+1]
                result += '_'
                i += 1
        else:
            if i+1 != len(txt):
                result += '_'

        count = 0

    i += 1

print (result)

2)

n = 5


if n<1 or n>20:
    print ('1 dan 20 oralig`igacha son yoz')
else:
    for i in range (0,n):
        print(i**2)
    
3)
i = 0

while i < 10:
    i += 1
    print (i)

4)
n = 5
result = []

for i in range (1,n+1):
    result.append(i)
    print (*result)


5)
n = int (input ('sonni kirit'))

sum = 0

for i in range (1, n+1):
    sum += i

print ("1 dan", n, "gacha bo'lgan sonlar yig'indisi:", sum)

6)
n = int (input ('son kirit'))

for i in range (1,n+1):
    if i % 2 == 0:
        print (i)

7)
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i>50 and i<=150:
        print (i)

8)
n = str(input ('son kirirt uzunligini topaman'))

i = 0
count = 0

while i < len(n):
    count += 1
    i += 1

print(count)

9)
n = int(input("n ni kiriting: "))

for i in range(n,0,-1):
    print (*range(i,0,-1))


10)
list1 = [10, 20, 30, 40, 50]
revers = list1[::-1]


for i in revers:
    print (i)

11)
for i in range (-10,0):
    print (i)

12)
a = 25
b = 50

prime = []

while a < b:
    i = 2
    is_prime = True

    while i*i <= a:
        if a % i == 0:
            is_prime = False
            break
        i += 1
        
    if is_prime:
        prime.append(a)

    a += 1

print(prime)

13)

n = 10

fib= [1,1]

while len(fib) < n:
    new_fib = fib[-1] + fib[-2]
    fib.append(new_fib)

print (fib)


14)
n = 5
fact = 1

for i in range (1,n+1):
    fact *= i

print(fact)


15)
list1 = [1, 1, 2] 
list2 = [2, 3, 4]

result =[]

for i in list1:
    if i not in list2:
        result.append(i)

for x in list2:
    if x not in list1:
        result.append(x)

print (result)

16)
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result2 = []

for i in list1:
    if i not in list2:
        result2.append(i)

for x in list2:
    if x not in list1:
        result2.append(x)

print(result2)


17)
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5,]

result3 = []

for i in list1:
    if i not in list2:
        result3.append(i)

for x in list2:
    if x not in list1:
        result3.append(x)

print (result3)
