# remove all occurrences of the element and return the length of new list.

def remove_element_old(my_list,val): #this changes the order of items in list
    start_index = len(my_list)-1
    for i in range(start_index,-1,-1):
        if my_list[i]==val:
            lst_index = len(my_list)-1
            my_list[i] = my_list[lst_index]
            my_list.pop()
            print(i,my_list,"after pop")

    return len(my_list)


def remove_element(my_list,val): 
    start_index = len(my_list)-1
    for i in range(start_index,-1,-1):
        if my_list[i]==val:
            for j in range(i,len(my_list)-1):
                my_list[j]=my_list[j+1]
            my_list.pop()

    return len(my_list)

'''
# Test case 1: Removing a single instance of a value (1) in the middle of the list.
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1
print("\nRemove a single instance of value", val1, "in the middle of the list.")
print("BEFORE:", nums1)
new_length1 = remove_element(nums1, val1)
print("AFTER:", nums1, "\nNew length:", new_length1)
print("-----------------------------------")

# Test case 3: Removing a value that's located at the start of the list.
nums3 = [-1, -2, -3, -4, -5]
val3 = -1
print("\nRemove value", val3, "that's located at the start of the list.")
print("BEFORE:", nums3)
new_length3 = remove_element(nums3, val3)
print("AFTER:", nums3, "\nNew length:", new_length3)
print("-----------------------------------")

# Test case 4: Attempting to remove a value from an empty list.
nums4 = []
val4 = 1
print("\nAttempt to remove value", val4, "from an empty list.")
print("BEFORE:", nums4)
new_length4 = remove_element(nums4, val4)
print("AFTER:", nums4, "\nNew length:", new_length4)
print("-----------------------------------")

# Test case 5: Removing all instances of a repeated value.
nums5 = [1, 1, 1, 1, 1]
val5 = 1
print("\nRemove all instances of value", val5, "from the list.")
print("BEFORE:", nums5)
new_length5 = remove_element(nums5, val5)
print("AFTER:", nums5, "\nNew length:", new_length5)
print("-----------------------------------")
'''

####################################################
#Write a Python function that takes a list of integers as input 
# and returns a tuple containing the maximum and minimum values in the list.

def find_max_min(myList):
    min,max = myList[0],myList[0]
    for num in myList:
        if num < min:
            min = num
        if num > max:
            max = num

    return(max,min)

#print( find_max_min([5, 3, 8, 1, 6, 9]) )

##########################################################
#Write a Python function called find_longest_string that takes a list of strings
# as an input and returns the longest string in the list. 
# The function should iterate through each string in the list, 
# check its length, and keep track of the longest string seen so far. 
# Once it has looped through all the strings, 
# the function should return the longest string found.

def find_longest_string(myStrings):
    lng_string = ""
    for string in myStrings:
        if len(string) > len(lng_string):
            lng_string = string

    return lng_string

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
#print(longest)  

########################################################
#Given a sorted list of integers, rearrange the list in-place 
# such that all unique elements appear at the beginning of the list.
#Your function should return the new length of the list containing only unique elements. 
# Note that you should not create a new list or use any additional data structures to solve this problem. 
# The original list should be modified in-place.

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#print(nums, list(set(nums)))

def remove_duplicates_old(my_list):
    if len(my_list)==0:
        return 0
    len_list = len(my_list)-1
    num = my_list[len_list]
    num_counter = 0
    new_length =1
    
    for i in range(len_list,-1,-1):
        #print(my_list,num,my_list[i])
        if num == my_list[i]:
            if num_counter !=0:
                my_list.append(my_list[i])
                my_list.pop(i)
            else:
                num_counter +=1
        else:
            num_counter =1
            num = my_list[i]
            new_length +=1

    print(my_list,new_length)
    return new_length

def remove_duplicates(nums): #compare the i+1 with i 
    if not nums:
        return 0
 
    write_pointer = 1
 
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
 
    print(nums)
    return write_pointer

#remove_duplicates(nums)
#############################################################
# Your task is to write a function called max_profit that takes the list of stock prices as input and 
# returns the maximum profit you can make by buying and selling at the right time.

#Note that you must buy the stock before selling it, 
# and you are allowed to make only one transaction (buy once and sell once).

def max_profit_old(prices):
    max = 0

    for i in range(1,len(prices)):
        for j in range(i):
            profit = prices[i] - prices[j]
            if profit > 0 and profit > max:
                max = profit

    return max


def max_profit(prices): # maintain a min values of the list at each iteration, the find profit for that iteration and maintain max value accordingly
    min_price = float('inf')
    max_profit = 0
 
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
 
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)

#print(profit)

#########################################################3333
#Function signature: def rotate(nums, k):

#Example:
#Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
#Function call: rotate(nums, k)
#Output: nums = [5, 6, 7, 1, 2, 3, 4]

def rotate_old(nums,k): #rotate list by k steps.
    i=0
    while i <k:
        nums.insert(0,nums[len(nums)-1])
        nums.pop()
        i+=1

def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
#print("Rotated array:", nums)

###########################################
#Given an array of integers nums, write a function max_subarray(nums) 
# that finds the contiguous subarray (containing at least one number) with the largest sum 
# and returns its sum.

#Remember to also account for an array with 0 items.

def max_subarray(my_list):
    if len(my_list) == 0:
        return 0
    max_val =my_list[0]
    sum_val = my_list[0]
    for num in my_list[1:]:
        sum_val = max(num,sum_val+num)
        if sum_val > max_val:
            max_val = sum_val
            
    return max_val
            
# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)
# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2) 

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3) 

