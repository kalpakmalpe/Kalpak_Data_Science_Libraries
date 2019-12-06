import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import sys


size = 1000
List_1=range(size)
List_2=range(size)


print("Size Of List",sys.getsizeof(1)*len(List_1))
#print(List_1)

Array_1 = np.array(range(1000))
Array_2 = np.array(range(1000))
#print(Array_1)
print("Size")
print("Size of array:",Array_1.size*Array_1.itemsize)
print(time.time())

list_3=np.array(range(size))
#print(type(list_3))
start_time=(time.time())
for x in range(len(List_1)):
    list_3[x]=List_2[x]+List_1[x]
#print(start_time)
print(list_3)
end_time=(time.time())
final=print(end_time-start_time)

start_time=time.time()
Array_3=Array_1+Array_2
end_time = time.time()
print("Time taken by Array",((end_time-start_time)*1000))
print(list_3)
print(Array_3)


#my_range_np_array = np.arange(1,24,2.002)
#random no graph
def func(x,y):
    c=x+y
    return c
array=np.fromfunction(func,(2,3),dtype="int64")  #here 2x3 is dimention of matrx
print(array)