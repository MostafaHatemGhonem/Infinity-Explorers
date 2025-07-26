

def multiply_elements(nums):
    result = 1
    for num in nums:
        result *= num
    return result


nums = [2, 4, 6, 2]
print(multiply_elements(nums))

print("#" * 10)

import math

nums = [2, 4, 6, 2]
print(math.prod(nums))



# Output
96
