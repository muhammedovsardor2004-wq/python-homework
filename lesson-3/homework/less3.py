1
my_list=['apple','orange','watermelon','banana','grape']
print(my_list[2])

2
my_list=[1,2,3,4,5,6]
new_list=[9,7,6,54,3,]

my_list.extend(new_list)

print(my_list)

3
first_list=my_list[0]
last_list=my_list[-1]
middle_list=my_list [len(my_list)//2]

new_list=[first_list,last_list,middle_list]
print(new_list)

4
my_list=['odam','yaxshilik','sardor','yaxshi','bola']
my_tuple=tuple(my_list)
print(my_tuple)
print(type(my_tuple))

5
my_list_cty=['tosh','sam','new york','navoi','paris']
my_list_cty
if 'paris' in my_list_cty:
    print('ha "paris" listni ichida bor')
else:
    print('afsus bu shaxar yuq listni ichida')


6
list_nam=[1,2,3,43,3,433,3,3,4,5,5,6,13,]
list_nam+=list_nam
print(list_nam)

7
last_first_list=[1,2,3,45,3,5,3,654,7,324,3]
last_first_list[0],last_first_list[-1]=last_first_list[-1],last_first_list[0]
print('yanilangan ruyxat:' ,last_first_list)

8
num_tuple=(1,2,3,4,5,6,7,8,9,10)
print (num_tuple[3:7])

9
color_list=['red','white','blac','blue','blue']
print(color_list.count('blue'))

10
animal_tuple=('wolf','rebbat','horse','lion')
print(animal_tuple.index('lion'))


11
num1_tuple=(9,8,7,6,5,4,3,2,1)
num2_tuple=(1,23,3,4,5,6,7,8,9)
new_tuple=num1_tuple+num2_tuple
print(new_tuple)

12
leng_list=[1,2,3,4,5,6,7,8]
leng_tuple=(1,2,3,4,5,6,7,8,9)

print('listni uzunligi:',len(leng_list))
print('tupleni uzunligi:',len(leng_tuple))

13
five_tuple=(1,2,3,4,5)

five_list=list(five_tuple)
print(five_list)
print(type(five_list))

14
max_min_tuple=(1,2,3,4,5,6,7,8)
print ('max qiymat:',max(max_min_tuple))
print ('min qiymat:',min(max_min_tuple))

15
reverse_tuple=('nima','gap','tinchmisan')

print('reversi qiymat:',reverse_tuple[::-1])

