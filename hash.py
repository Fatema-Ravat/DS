class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,":",val)

    def set_item(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
        return True
    
    #gets value of the given key
    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
                
        return None
    
    # returns all the keys of the hashtable
    def keys(self):
        all_keys = []
        for val in self.data_map:
            if val:
                for i in range(len(val)):
                    all_keys.append(val[i][0])
        
        return all_keys
    
    def values(self):
        all_values = []
        for val in self.data_map:
            if val:
                for i in range(len(val)):
                    all_values.append(val[i][1])
        
        return all_values

def item_in_common(list1,list2):
    my_dict ={}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False

def find_duplicates(nums):
    my_dict = {}
    final_list = []
    
    for val in nums:
        if val in my_dict:
            if val not in final_list:
                final_list.append(val)
            my_dict[val] = my_dict[val] +1
        else:
            my_dict[val] = 1
            
    print(final_list, my_dict)    
    return final_list

def first_non_repeating_char(str):
    my_dict ={}
    i = 0
    for ch in str:
        my_dict[ch] = my_dict.get(ch, 0) + 1
        '''
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] = my_dict[ch] +1
        '''
    
    print(my_dict)
    for key in my_dict:
        if my_dict[key] == 1:
            return key
    return None


def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        print(canonical)
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    print(anagram_groups)
    return list(anagram_groups.values())
        

def two_sum(nums,target):
    my_dict = {}
    for i,num in enumerate(nums):
        for key in my_dict:
            if (my_dict[key] + num )==target:
                return [key,i]
        my_dict[i] = num
        print(my_dict)  
    return []

def subarray_sum(nums,target):
    my_dict = {}
    
    for i, num in enumerate(nums):
        if num == target:
            return [i,i]
        for key in my_dict:
            if (my_dict[key] + num) == target:
                return [key,i]
            else:
                my_dict[key] = my_dict.get(key)+num
        
        my_dict[i] = num  
        print(my_dict)
        

    return[]

# remove duplicates from the given list and return the list
def remove_duplicates(my_list):
    new_list = list(set(my_list))
    return new_list

def has_unique_chars(my_string):
    or_len = len(my_string)
    set_len  = len(set(my_string))
    return True if (or_len == set_len) else False
    #return True if (len(my_string)== len(set(my_string))) else False

#print(has_unique_chars('fdshfa'))

def find_pairs(arr1,arr2,target):
    
    if len(arr1) == 0 or len(arr2) == 0:
        return []

    mid_index = len(arr2)%2
    pairs = []
    for i in arr1:    
        if (i+arr2[mid_index]) == target:
            pairs.append((i,arr2[mid_index]))
        elif (i+arr2[mid_index]) < target:
            for j in range(mid_index,len(arr2),1):
                if ( i + arr2[j]) == target:
                    pairs.append((i,arr2[j]))
        else:
            for j in range(mid_index,-1,-1):
                if ( i + arr2[j]) == target:
                    pairs.append((i,arr2[j]))
    print(pairs)
    return pairs

''' better way of coding
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs()
'''
arr1 = [-1, 0, 1]
arr2 = [-1, 0, 1]
target = 0

#pairs = find_pairs(arr1, arr2, target)

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    old_seq = 0
    for num in nums:
        temp =num
        seq = 1
        while temp+1 in num_set:
            seq +=1
            temp +=1
        if seq>old_seq:
            old_seq = seq
        
    return(old_seq)



list1 = [1,3,5]
list2 = [2,4,5]

'''
nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )


print(two_sum([5, 1, 7, 2, 9, 3], 10)) 
print(two_sum([4, 2, 11, 7, 6, 3], 9))


group_anagrams(["eat", "tea"])

print(first_non_repeating_char('aabbcc'))

find_duplicates([1, 2, 3, 4, 5]) 
find_duplicates([1, 1, 2, 2, 3]) 
find_duplicates([1, 1, 1, 1, 1])
find_duplicates([1, 'a', 2, 'b'])




#print(item_in_common(list1, list2))



my_hash = HashTable()

my_hash.set_item('bolts',1000)
my_hash.set_item('nuts',1000)
my_hash.set_item('washers',500)
my_hash.print_table()

print(my_hash.get_item('washers'),my_hash.keys(),my_hash.values())
'''