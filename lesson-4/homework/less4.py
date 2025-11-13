1
my_dict = {'ali':20,'vali':30,'jon':10}

my_dict_asc = dict( sorted(my_dict.items(), key=lambda item: item[1]) )
my_dict_desc = dict( sorted(my_dict.items(), key=lambda item: item[1], reverse=True) )
                    
print('Ascending',my_dict_asc)
print('Descending',my_dict_desc)

2
add_dict = {0:10, 1:20}

add_dict.update({2:30})

print (add_dict)

3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1.update(dic2)
dic1.update(dic3)

all_dic=dic1.copy()

print (all_dic)

4
n = int(input('xoxlagan soningdi kirirt bratishkam'))

loop_dic = {}

for x in range(1,n+1):
    loop_dic[x] = x*x

print(loop_dic)


5
loop15_dict = {}

for x in range(1,15+1):
    loop15_dict[x]=x**2

print(loop15_dict)

6
create_set = {11,1,1,1,1,2,2,33,3,4,44,4,4,4,5,5,5,6,7,6,'salom'}
print(create_set)

7
create_set = {11,1,1,1,1,2,2,33,3,4,44,4,4,4,5,5,5,6,7,6,'salom'}

create_set

for new_set in create_set:
    print(new_set)

8
create_set = {11,1,1,1,1,2,2,33,3,4,44,4,4,4,5,5,5,6,7,6,'salom'}

create_set.add(45)
print(create_set)

9
create_set = {11,1,1,1,1,2,2,33,3,4,44,4,4,4,5,5,5,6,7,6,'salom'}

create_set.remove(5)
print(create_set)

10

create_set = {11,1,1,1,1,2,2,33,3,4,44,4,4,4,5,5,5,6,7,6,'salom'}

create_set.discard(1)
print(create_set)
