counter =0 
def fib_nonmemo(n):
    global counter
    counter +=1
    if n == 1 or n==0:
        return n
    result = fib_nonmemo(n-1)+fib_nonmemo(n-2)
    return result

#print("old fib:",fib_nonmemo(30),counter) # 1,1 answer = 1

#fib(7) - 41 function calls
#fib(20) - 21891 fuction calls
#so you can see that function calls increases exponentially. This is ineffecient.
#USER MEMONIZATION(Dynamic programing) to make it efficient

# this is top-down way of solving
memo = [None]*100 # define list for storing 100 values. initialized to None
new_counter =0 
def fib(n):
    global new_counter
    new_counter +=1
    if memo[n] is not None: #checking if value first avialable in list
        return memo[n]
    if n==0 or n==1:
        return n
    memo[n] =  fib(n-1)+fib(n-2)
     
    return memo[n]

#print("new fib:",fib(30),new_counter)

# solving fibonacci sequence in bottom-up approcah

def fib_bottomup(n):
    fib_list = [0,1]
    for i in range(2,n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list[n]

print("bottom up fib:",fib_bottomup(10))