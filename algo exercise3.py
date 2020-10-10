# -*- coding: utf-8 -*-
from __future__ import print_function, division
import numpy as np
import timeit
from timeit import Timer
import random

# create a list of random number
def random_list_input(start, stop, length): 
    
    if start >= stop:
        start, stop = (int(start), int(stop))
    
    length = int(abs(length))

    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

# define the process of merging
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

target_list = [10, 100, 1000, 10000]

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
def test_merge1000():
    i = target_list[2]
    merge_sort(random_list_input(1, i, i))
def test_sorted1000():
    i = target_list[2]
    sorted(random_list_input(1, i, i))
def test_merge10000():
    i = target_list[3]
    merge_sort(random_list_input(1, i, i))
def test_sorted10000():
    i = target_list[3]
    sorted(random_list_input(1, i, i))


# calculate the processing time in mergesort
type_two_kinds = ['sorted', 'merge']

for i in target_list:
    for m in type_two_kinds:
        text_original = 'test_' + m + str(i)
        text_original2 = 'test_' + m + str(i) + '()'
        text_target = 'from __main__ import test_' + m + str(i)

        timer = Timer(stmt = text_original2, setup = str(text_target))
        print(text_original + ': ' + str(timer.timeit(100)))



'''   
scratch
   
# calculate the processing time in BIF sorted  
for i in target_list:
    text_original = 'test_sorted' + str(i)
    text_original2 = 'test_sorted' + str(i) + '()'
    text_merge = 'from __main__ import test_sorted' + str(i)
    text_sorted = 'from __main__ import test_sorted' + str(i)
    
    timer_merge = Timer(stmt = text_original2, setup = str(text_merge))
    print(text_original + ': ' + str(timer_merge.timeit(100)))
    
 
timer_merge10 = Timer("test_merge10()", "from __main__ import test_merge10")
print("timer_merge10:", timer_merge10.timeit(100))
timer_sorted10 = Timer("test_sorted10()", "from __main__ import test_sorted10")
print("timer_sorted10:", timer_sorted10.timeit(100))

timer_merge100 = Timer("test_merge100()", "from __main__ import test_merge100")
print("timer_merge100:", timer_merge100.timeit(100))
timer_sorted100 = Timer("test_sorted100()", "from __main__ import test_sorted100")
print("timer_sorted100:", timer_sorted100.timeit(100))

timer_merge1000 = Timer("test_merge1000()", "from __main__ import test_merge1000")
print("timer_merge1000:", timer_merge1000.timeit(100))
timer_sorted1000 = Timer("test_sorted1000()", "from __main__ import test_sorted1000")
print("timer_sorted1000:", timer_sorted1000.timeit(100))

timer_merge10000 = Timer("test_merge10000()", "from __main__ import test_merge10000")
print("timer_merge10000:", timer_merge10000.timeit(100))
timer_sorted10000 = Timer("test_sorted10000()", "from __main__ import test_sorted10000")
print("timer_sorted10000:", timer_sorted10000.timeit(100))
'''