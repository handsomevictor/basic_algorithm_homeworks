# -*- coding: utf-8 -*-
from __future__ import print_function, division
from timeit import Timer
import random


# ----------------------------------------------------------------------------
# create a list of random number, which will be used as a parameter in merge_sort()
def random_list_input(start, stop, length): 
    
    if start >= stop:
        start, stop = (int(start), int(stop))
    
    length = int(abs(length))

    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


# ----------------------------------------------------------------------------
# define the process of merging, exactly the same codes as the one in No.2
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

# define mergesort halfing process
def merge_sort(list1):
    if len(list(list1)) <= 1:
        return list1
    
    middle = int(len(list1) / 2)
    left = merge_sort(list1[ :middle])
    right = merge_sort(list1[middle: ])
    return merge(left, right)


# ----------------------------------------------------------------------------
# to make it all clear, after searching how to use Timer, I would like to define 
# every situation out individually, because if I define them as one function with  
# a parameter, the real running time will be not accurate (because there is a loop in 
# those functions so each time Python calculate the running time of processing 10 numbers, 
# 10000 numbers will be generated, which will make the process redundant).

# all the following functions are senarios demanded in the question

def test_merge10(): 
    i = target_list[0]
    merge_sort(random_list_input(1, i, i))
def test_sorted10():
    i = target_list[0]
    sorted(random_list_input(1, i, i))
def test_merge100():
    i = target_list[1]
    merge_sort(random_list_input(1, i, i))
def test_sorted100():
    i = target_list[1]
    sorted(random_list_input(1, i, i))
def test_merge500():
    i = target_list[2]
    merge_sort(random_list_input(1, i, i))
def test_sorted500():
    i = target_list[2]
    sorted(random_list_input(1, i, i))    
def test_merge1000():
    i = target_list[3]
    merge_sort(random_list_input(1, i, i))
def test_sorted1000():
    i = target_list[3]
    sorted(random_list_input(1, i, i))   
def test_merge2000():
    i = target_list[4]
    merge_sort(random_list_input(1, i, i))
def test_sorted2000():
    i = target_list[4]
    sorted(random_list_input(1, i, i))
def test_merge3000():
    i = target_list[5]
    merge_sort(random_list_input(1, i, i))
def test_sorted3000():
    i = target_list[5]
    sorted(random_list_input(1, i, i))
def test_merge4000():
    i = target_list[6]
    merge_sort(random_list_input(1, i, i))
def test_sorted4000():
    i = target_list[6]
    sorted(random_list_input(1, i, i))    
def test_merge5000():
    i = target_list[7]
    merge_sort(random_list_input(1, i, i))
def test_sorted5000():
    i = target_list[7]
    sorted(random_list_input(1, i, i))
def test_merge6000():
    i = target_list[8]
    merge_sort(random_list_input(1, i, i))
def test_sorted6000():
    i = target_list[8]
    sorted(random_list_input(1, i, i))    
def test_merge7000():
    i = target_list[9]
    merge_sort(random_list_input(1, i, i))
def test_sorted7000():
    i = target_list[9]
    sorted(random_list_input(1, i, i))
def test_sorted8000():
    i = target_list[10]
    sorted(random_list_input(1, i, i))    
def test_merge8000():
    i = target_list[10]
    merge_sort(random_list_input(1, i, i))
def test_sorted9000():
    i = target_list[11]
    sorted(random_list_input(1, i, i))
def test_merge9000():
    i = target_list[11]
    merge_sort(random_list_input(1, i, i))
def test_sorted10000():
    i = target_list[12]
    sorted(random_list_input(1, i, i))
def test_merge10000():
    i = target_list[12]
    merge_sort(random_list_input(1, i, i))
    
# calculate the processing time in merge_sort
type_two_kinds = ['sorted', 'merge']
target_list = [10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
# these three are for plotting
for_plottingx = []
for_plottingy = []
for_plot_kind = []

# to make it concise, we use a loop to print the processing time of each function above
for i in target_list:
    for m in type_two_kinds:
        text_original = 'test_' + m + ' of ' + str(i) + ' numbers'
        text_original2 = 'test_' + m + str(i) + '()'
        text_target = 'from __main__ import test_' + m + str(i)

        timer = Timer(stmt = text_original2, setup = str(text_target))
        
        # for plotting
        for_plottingy.append(timer.timeit(number=100))
        for_plottingx.append(i)
        for_plot_kind.append(m)
        
        A = text_original + ': ' + str(timer.timeit(100))
        print(A)
# ---------------------------------------------------------------------------- 
# for plotting
import matplotlib.pyplot as plt
for_sorted_plot = []
for_merged_plot = []
target_list = [10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

for i in range(1, len(for_plottingy), 2):
    for_merged_plot.append(for_plottingy[i])
for i in range(0, len(for_plottingy), 2):
    for_sorted_plot.append(for_plottingy[i])

plt.plot(target_list, for_sorted_plot)
plt.plot(target_list, for_merged_plot)
plt.xlabel('number of random numbers') 
plt.ylabel('real processing time')
plt.legend(["sorted()", "merge sort"])
plt.show()

# the findings:
'''
result:
1.  the running time of using our own mergesort algorithm on a certain amount of
    data is always longer than the python Built In Function sorted().
    So, sorted() is always faster than ours. 
2.  the larger amount of test number, the longer of time it would take both our own
    mergesort algorithm and the BIF sorted() longer time to process.
3.  The O notation of our mergesort is n*log(n)
    By consulting the internet we knew that the O notation of Timsort sorted()
    is n*log(n)
    So actually the mergesort we wrote has the same time complexity as the built 
    in function sorted().

'''



