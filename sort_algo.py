def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i): # go from 0 to end of list each time and compare
            if my_list[j]>my_list[j+1]:
                temp = my_list[j]
                my_list[j]= my_list[j+1]
                my_list[j+1] = temp
        #at end of the j for loop each time greatest number will bubble to the end.
    
    return my_list

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1,len(my_list)):
            if my_list[j]<my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index]= temp
        # at the end of each j for loop iteration and swap, min value move the front of list.
    return my_list

def insertion_sort_old(my_list): # O(n*n)

    for i in range(len(my_list)-1):
        for j in range(i+1,0,-1):
            if my_list[j]<my_list[j-1]:
                temp = my_list[j]
                my_list[j]=my_list[j-1]
                my_list[j-1]= temp
        # at end of j for loop the smallest value will move the front.

    return my_list
def insertion_sort(my_list): # if almost sorted then o(n)
    for i in range(1,len(my_list)):
        temp = my_list[i]
        j= i-1
        while j>-1 and temp<my_list[j]: #moving towards 0 in the list
            my_list[j+1]=my_list[j]
            my_list[j] = temp
            j -=1
        # at the end of this while loop, if list[i] will move into its appropriate position in the list

    return my_list

# merges 2 sorted list
def merge(list1,list2):
    new_list =[]
    i,j = 0,0

    while i < len(list1) and j <len(list2):
        if list1[i]<list2[j]:
            new_list.append(list1[i])
            i+=1
        else: 
            new_list.append(list2[j])
            j+=1
     
    while j<len(list2):
        new_list.append(list2[j])
        j+=1
    while i<len(list1):
        new_list.append(list1[i])
        i+=1

    return new_list

def merge_sort(my_list):
    if len(my_list) ==1:
        return my_list
    
    mid_index = len(my_list)//2
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left,right)

def pivot(my_list,pivot_index,end_index):
    print("start pivot",my_list,pivot_index,end_index)
    swap = pivot_index
    
    for i in range(pivot_index+1,end_index+1):
        print("i,pivot_index",i,pivot_index)
        if my_list[i] < my_list[pivot_index]:
            swap +=1
            my_list[swap],my_list[i] = my_list[i],my_list[swap]
        
    my_list[pivot_index],my_list[swap]=my_list[swap],my_list[pivot_index]
    pivot_index = swap
    print(my_list,pivot_index,end_index,"in pivot")
    return pivot_index

def quick_sort(my_list,left,right):
    if left<right:
        pivot_index = pivot(my_list,left,right)
        quick_sort(my_list,left,pivot_index-1)
        quick_sort(my_list,pivot_index+1,right)
    return my_list

'''
print("bubble sort:",bubble_sort([4,2,6,5,1,3]))
print("selection sort:",selection_sort([4,2,6,5,1,3]))
print("insertion sort:",insertion_sort([4,2,6,5,1,3]))
print("merge:",merge([1,3,7,8],[2,4,5,6]))
print("merge sort:",merge_sort([4,2,6,5,1,3]))

print("pivot:",pivot([4,6,1,7,3,2,5],0,6))'''
print("quick sort:",quick_sort([4,6,1,7,3,2,5],0,6))