# -*- coding: utf-8 -*-


# define mergesort halfing process with recursive function
def merge_sort(list1):
    # if there is only one element in the array or it's empty, return the original array
    if len(list(list1)) <= 1:
        return list1
    
    # if the length satisfies the demand, we start to divide it into 2 pieces each loop, and the final
    # target is to splid the original array into pieces that only contain 1 element each.
    middle = int(len(list1) / 2)
    # use recursive function to help us spliting the array to the smallest pieces
    left = merge_sort(list1[ :middle])
    right = merge_sort(list1[middle: ])
    
    # after spliting the array into smallest pieces, we begin to merge it, and the merge function is defined below
    return merge(left, right)


# define the process of merging with two list parameters a and, and our aim is to make a and b into one array of 
# the ascending order
def merge(a, b):
    
    # we will put the ordered a and b list into an empty list c, so create an empty one
    c = []
    h = j = 0
    while j < len(a) and h < len(b):    # compare each element, and choose the smaller one to add into the empty list c
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    # we should also process the rest numbers which were not compared in the previous loop
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

# the original list
B_list = [510, 57, 512, 38, 909, 241, 897, 250, 653, 499, 154, 511, 612, 677, 865, 777]

print(merge_sort(B_list))


    