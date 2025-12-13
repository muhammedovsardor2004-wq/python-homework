#1

import numpy as np

my_list = [12.23, 13.32, 100, 36.32] 

np_1d = np.array(my_list)

print("Original List:", my_list)
print("One-dimensional NumPy array:", np_1d)


#2
import numpy as np

matrix = np.arange(2,11).reshape(3,3)

print(matrix)


#3
import numpy as np

vector = np.zeros(10)
print(vector)

vector[5] = 11

print(vector)


#4
import numpy as np

nums = np.arange(12,38)

print(nums)


#5
import numpy as np

my_array = np.array([1,2,3,4])

my_float = my_array.astype(float)

print(type(my_float))




#6

import numpy as np

fahrenheit = np.array([0, 12, 45.21, 34, 99.91, 32])

celsius = (5/9) * (fahrenheit - 32)
fahrenheit_back = (9/5) * celsius + 32

print("Values in Fahrenheit degrees:", fahrenheit)
print("Values in Centigrade degrees:", np.round(celsius, 2))
print("Values in Centigrade degrees:", np.round(celsius, 2))
print("Values in Fahrenheit degrees:", np.round(fahrenheit_back, 2))


#7
import numpy as np

my_array = np.array([10,20,30])

new_array = np.append(my_array,[40, 50, 60, 70, 80, 90])

print("Original array:", my_array)

print("After append values to the end of the array:", new_array)


#8
import numpy as np

randoms = np.random.rand(10)

mean_val = np.mean(randoms)
median_val = np.median(randoms)
std_val = np.std(randoms)

print("Random array:", randoms)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)


#9

import numpy as np

random = np.random.rand(10,10)

max_val = np.max(random)
min_val = np.min(random)

print("10x10 Random Array:\n", random)
print("Minimum value:", min_val)
print("Maximum value:", max_val)


#10
import numpy as np

random_3d = np.random.rand(3,3,3)

print('3d random values:\n', random_3d)
