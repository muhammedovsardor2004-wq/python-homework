1
name = input('Ismingizni kiriting')
years = int (input('Tug`ulgan yilingizni  kiriting'))
current_year = 2025 
result = current_year-years

print ('Salom', name.capitalize()+'!')
print('Sizning yoshingiz', result , 'da')

2)
car_name = 'LMaasleitbtui'

print (car_name[::2])

3)
car_name='MsaatmiazD'

print(car_name[::2])

4)
city =  "I'am John. I am from London"
residence=city [city.index('L'):]

print(residence)

5)
name = input('Ismingizni kiriting').capitalize()
result=name[::-1]

print(result)

6)
name=input('xoxlaganingdi yoz').lower()
a=name.count('a')
e=name.count('e')
o=name.count('o')
u=name.count('u')
i=name.count('i')

print('Unli harflar soni',a+e+o+u+i,'ta')

7)
num=list( map( int , input('xoxlagan soningdi space bn kirit').split()))
print(max(num))

8)

word=input('xoxlagan suzingdi kirit meni uni palendrommi yoki yuqligini aytaman').lower().replace(' ','')

if word==word[::-1]:
    print ('bu so`z palindrom')
else:
    print ('bu so`z palindrom emas')

9)
email=input('email kirit')

if '@' in email:
    result = email.split('@')[1]
    print('Domain;',result)
else:
    print('emailda "@" yuq tekshiring')

10)
import random
import string

len=12

stringss=string.ascii_letters
nums=string.digits
other="!@#$%^&*()"

all_char=stringss+nums+other

password=''.join(random.choices(all_char,k=len))

print('Sizning kodinggiz:',password)


