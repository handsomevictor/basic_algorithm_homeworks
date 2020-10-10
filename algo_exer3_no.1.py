# -*- coding: utf-8 -*-

# define the insertion sort with binary search
def insertion_sort(arr):

    count = 0   # this variable is used for calculating the number of comparison in each sort step of the array
    print('comparison time is: ' + str(count))
    print(A_list)   # print the original list for reference
    num = len(arr)  # get the length of the target array

    for i in range(1, num):
        left = 0
        right = i - 1
        temp = arr[i]
        comparison_time = 0
        while left <= right:    # once left is larger than right, jump out of the loop
            mid = (left + right) // 2   # get the middle number of left and right, and make it to integer
            
            # compare the middle number and the inserting number
            if arr[mid] < temp: # 
                left = mid + 1
            else:
                right = mid - 1
            count += 1  # we need to calculate the comparison time of each loop
            comparison_time += 1    # we need to calculate the total comparison time of all loops
        
        j = i - 1   # find the position that the variable temp should be inserted, and move the numbers after left backward one position
        while j >= left:
            arr[j + 1] = arr[j]
            j -= 1

        arr[left] = temp    # now we put the insertion number into the left position
        print('comparison time is: ' + str(comparison_time))    # print the outcome of each comparison time in each loop
        print(arr)  # for reference, print the latest modified array

    print('the total comparison times is: ' + str(count))

# the original list
A_list = [503, 87, 512, 61, 908, 170, 897, 275, 654, 426, 154, 509, 612, 653, 765, 703]

# use the function we defined
insertion_sort(A_list)
