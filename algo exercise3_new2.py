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

def test_merge():
    for i in target_list:
        merge_sort(random_list_input(1, i, i))
def test_sorted():
    for i in target_list:
        sorted(random_list_input(1, i, i))

type_two_kinds = ['sorted', 'merge']

for i in target_list:
    for m in type_two_kinds:
        
        # text_original = 'test_' + m 
        text_original2 = 'test_' + m + '()'
        text_target = 'from __main__ import test_' + m

        timer = Timer(stmt = text_original2, setup = str(text_target))
        print('for ' + m + ', the time of ' + str(target_list[target_list.index(i)]) + ' numbers will take:' + str(timer.timeit(100)))
        
        # print(text_original + ': ' + str(timer.timeit(100)))


