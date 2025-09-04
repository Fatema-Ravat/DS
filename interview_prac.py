#Reverse the input string
def reverse_str(st):
    return st[::-1]

#print(reverse_str("Hello"))


#Check palindrom
def check_palindrom(st):
    return st.lower()==st[::-1].lower()

#print(check_palindrom("Helleh"))


#check if a number is repeated in a list on 1 to N numbers and return repeated number.
def check_repitition(nums,n):
    sum_num = sum(nums)
    sum_act = sum(n for n in range(1,n+1))
    print(sum_num,sum_act)
    if sum_num == sum_act:
        return (False,0)
    else:
        return(True,sum_num-sum_act)

#print(check_repitition([1,3,4,5,2,2],5))

#find the factorial
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

#print(f"factorial of 3: {fact(3)}")

#print fibonacci upto n
def fib_series(n):
    l = [0,1]
    for i in range(2,n):
        num=l[i-1]+l[i-2]
        l.append(num)
    print(f" series is : {l}, sum of it is {sum(l)}")

#fib_series(4)

#find largest number of list [21,34,45,12,11]
print(f"largest number of list: {max([21,34,45,12,11])}")

#count ocurrences of each word in a string
def count_words(sentence):
    l_sentence = sentence.split()
    s_dict={}
    for word in l_sentence:
        if word.lower() in s_dict:
            s_dict[word.lower()] +=1
        else:
            s_dict[word.lower()]=1
    print(s_dict)

#count_words("Hello world world is beautiful hello to you")


#another method:
from collections import Counter
def word_count(s):
    words = s.split()
    print( dict(Counter(words)))

#word_count("Hello world world is beautiful hello to you")

#remove duplicatess from a list
def remove_dup(l):
    return list(set(l))

#print(remove_dup([1,2,3,14,1,3]))

#check if 2 strings are anagram
def check_anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        print(f"{s1} and {s2} are anagrams")
    else:
        print(f"{s1} and {s2} are NOT anagrams")

#check_anagram("earth","thar")

#find 2nd largest number in list
def second_largest(l):
    largest = max(l)
    s_large = (l[0] if l[0]<largest else 0)
    print(s_large)
    for num in l[1:]:
        if num>s_large and num!=largest:
            s_large=num
    print(f"Second largest number is {s_large}")

def sec_large(l):
    unique_num = list(set(l))
    unique_num.sort()
    print(unique_num[-2])

#second_largest([242,99,53,23,92])
#sec_large([242,99,53,23,92])

#flatten the nested list #recursive solution #better as it will flatten all nested list
def flaten_list(l1):
    fl=[]
    for item in l1:
        if isinstance(item,int):
            fl.append(item)
        else:
            fl.extend(flaten_list(item))
    return fl
print(flaten_list([1,2,[4,[3,8]],[5,6],9]))    

#itertools solution ## it cannot flatten if ints are there in the list , only list in list
import itertools

print(list(itertools.chain.from_iterable([[4,3,8],[5,6]])))

#for loop solution
def func(l1):
    fl =[]
    for i in l1:
        if isinstance(i,int):
            fl.append(i)
        else:
            for j in i:
                fl.append(j)
    print(fl)

#func([1,2,[4,3],[5,6],9])


#merge 2 sorted list
def merge_sorted_list(l1,l2):
    l1.extend(l2)
    return sorted(l1)

#print(merge_sorted_list([2,4,8,9],[1,7,11]))



#find prime number upto n
def find_prime(n):
    prime =[]
    for num in range(2,n+1):
        is_prime = True
        for div in range(2,int(num*0.5)):
            if (num %div)==0:
                is_prime = False
                break
        if is_prime:
            prime.append(num)
    print(prime)

#find_prime(20)


#check if number is armstrong (sum of digits to the power of number of digits = original no.)


#find intersection of 2 lists #brute force
def find_intersection_bf(l1,l2):
    intersection =[]
    for num1 in l1:
        for num2 in l2:
            if num1==num2:
                intersection.append(num1)
                break
    print(intersection)

def find_intersection_(l1,l2):
    intersection = []
    l1_dict={}
    for num in l1:
        l1_dict[num]=True
    for num in l2:
        if num in l1_dict:
            intersection.append(num)

    print(intersection)

def find_intersection(l1,l2):
    print( list(set(l1) & set(l2)))

#find_intersection([1,4,3,7,2],[1,0,9,2])


#first non-repeated character in string
def find_nonrepeat_(st):
    st_dict={}
    for i, s in enumerate(st):
        if s not in st_dict:
            st_dict[s] = i
        else:
            st_dict.pop(s)
    print(next(iter(st_dict)))

def find_nonrepeat(st):
    f = Counter(st)
    for item in st:
        if f[item] == 1:
            return item
    return None

print(find_nonrepeat("helloeh"))

#rotate a list by k elements i/p [1,2,3,4,5] k=2 o/p=> [4,5,1,2,3]
def rotate_list(l1,k):
    k2 = len(l1)-k
    print(l1[k2:] + l1[:k2])

rotate_list([1,2,3,4,5],2)

#find pairs in array with given sum
def find_sum_pairs(l1,sum):
    s = set()
    pairs =[]
    for num1 in l1:
        num2 = sum-num1
        if num2 not in s:
            pairs.append((num1,num2))
            s.add(num1)               
    return pairs

#print(find_sum_pairs([1,2,3,4,5,6],7))


#implement binary serach


#implement stack using list

#########################################################
#### list mutable and immutable datatypes 
# Immutable - int,string,float,tuple,frozenset
# Mutable - list,set,dict,bytearray

x="hello"
print(id(x))#mem address
x +="world"
print(id(x)) #this address is different as its immutable type



#shallow vs deepcopy vs assignment

list1 = [10,[11,23],[11,13,[33,55],24]]
import copy
shallow = list1.copy()
deep = copy.deepcopy(list1)
assign = list1
print(list1,shallow,deep,assign)
shallow[1][0]=111
print(list1,shallow,deep,assign)
assign[1][1]=100
assign[0]=222
print(list1,shallow,deep,assign)


#### implement a decorator
def log(func): #how to pass values to decorator?
    def wrapper(*args,**kwargs):
        print("Logging func")
        result = func(*args,**kwargs)
        print(f"{func,__name__} return")
        return result
    return wrapper

@log
def func(a,b):
    return a+b

print(func(3,4)) 

#decorator with arguments.
"""
    def repeat(times):
        def decorator(func):
            def wrapper(*args,**kwargs):
                print("In the decorator")
                for _ in range(times):
                    func()
            return wrapper
        return decorator
"""

##### generators

def square(n):
    for num in range(1,n+1):
        yield num*num

gen = square(5)
print(next(gen)) #1
print(next(gen)) #4
#values are returned 1 by 1 , can loop through it using for loop, 
# also once the value is used cant go back.
for num in gen:
    print(num)

#### iterating through list using iter and next
list1 = [1,2,3,4,5]
#print(next(list1)) -- This gives error that list1 is not iterator
print(next(iter(list1)))


#### difference between is and == (== compares values is compares object)


list1 = [1,2,3]
list2 =list1
list3 = list1.copy()

print(f"for list1 and list2 == {list1==list2} is {list1 is list2}")
print(f"for list1 and list3 == {list1==list3} is {list1 is list3}")

##### list comprehension

cubes = [n*n*n for n in range(10) if n%2 ==0 ] # gives cubes of only even numbes
print(cubes)

##### python @classmethod , @staticmethod and instance method
# what vars of class can a classmethod,static and instance access 
class Test:
    cl_var ="class"
    def __init__(self):
        self.ints = "instance"

    @classmethod
    def class_method(cls):
        return "Its a class method" +cls.cl_var
        #can acess only class method and variables
    
    @staticmethod
    def static_method():
        return "This is static mthd"
        #cannot access unless vars passed
    
    def instance_method(self):    
        return "this is instance method"+self.ints + Test.cl_var
        #can access all
    
##### difference between __new__ and __init__
#new is called when the object is created (before init), init is called when object is initialized(constructor)
class Test1:
    def __new__(cls,*args):
        print("In __new__")
        return super().__new__(cls)

    def __init__(self, val):
        self.val = val
        print("in __init__")
        
Test1(1)

###### how to make a class iterable
# impletment __iter__ , __next__, __init__ and raise StopIteration

class Counter:
    def __init__(self,n):
        self.n = n 
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <=self.n:
            self.current +=1
            return self.current
        else:
            raise StopIteration
        
for num in Counter(5):
    print(num) #1,2,3,4,5

#### @property decorator for a method in class
#when this is used, the that method can be used as attribute.

class Square:
    def __init__(self,x):
        self.x =x
    
    @property
    def area(self):
        return self.x*self.x

s= Square(5)
print(s.area) #no brackets required.



##### context manager => Helps manage resource(files,network conn,locks) by automatically 
# setting and cleaning on entering and exiting < used with 'with' statement>

# can be created as class containing __enter__, __exit__ methods
# a method can be made using contextlib.contextmanager decorator and using yield for resource.

#without context manager:
f = open("example.txt","w")
f.write("Hello")
f.close() # you might forget this or an exception might occur before this.

#with context 
with open("example.txt","w") as f:
    f.write("Hello")
#file automatically closed even if exception occurs.

#CUSTOM context manager:




#### lamda, map, reduce, filter, sorted functions.
# lamda => lamda x,y:x+y -- its an annonymous function that takes input variables:expression
# map(function, iterator) => the function is applied on each element of the iterator
# filter(function, iterator) => the function is applied on each element and only that return True are returned
# sorted(iterator,key(function)) => iterator to be sorted and what key to use for sorting
# reduce()

square = lambda x:x**2
print(square(10))


# dict  d={k:v} d.keys()=>gives keys d.values()=>gives values d.items()=>(k,v)pairs.  


#### dataclass

#### closure
### monkey patching
### __slots__
#### abstract classes and interfaces(protocols)