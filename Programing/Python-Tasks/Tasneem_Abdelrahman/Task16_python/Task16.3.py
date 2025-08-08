def multiply(numbers): 
    result=1
    for num in numbers: 
        result*=num
    return result

nums = [2, 4, 6, 2]    
print(multiply(nums)) 


from functools import reduce
def multiply (n1,n2,): 
    return n1*n2
nums=[2,4,6,2]
result=reduce(multiply,nums) 
print(result) 

nums=[2,4,6,2]
result=reduce(lambda n1,n2: n1*n2, nums)
print(result) 
