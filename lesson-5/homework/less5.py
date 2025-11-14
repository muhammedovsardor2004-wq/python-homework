1

a)
year = 2000

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print (f'{year} is leap year')
        else:
            print (f'{year} is not leap year')

    else:
        print (f'{year} is leap year')
else:
    print (f'{year} is not leap year')

b)
year = 1000

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print (f'{year} is leap year') 
else:
    print (f'{year} is not leap year')


2

n = int (input ('sonni kirit'))

if n<1 or n>100:
     print("Xatolik: n 1 dan 100 gacha bo'lishi kerak")

else:
    if n % 2 == 1:
        print ('Weird')

    elif n % 2 == 0 and n in range(2,6):
        print ('Not Weird')

    elif n % 2 == 0 and n in range(6,21):
        print ('Weird')

    elif n % 2 == 0 and n>20:
        print ('Not Weird')



3

a)
a = int(input('1 - sonni kirit: '))
b = int(input('2 - sonni kirit: '))

if a % 2 == 0:
    num = a
else:
    num = a+1

even_nums1 = list(range (num,b+1,2) )

print (even_nums)

b)
a = int(input('1 - sonni kirit: '))
b = int(input('2 - sonni kirit: '))

even_nums2 = list (range(a + a % 2,  b + 1,  2))

print (even_nums2)
