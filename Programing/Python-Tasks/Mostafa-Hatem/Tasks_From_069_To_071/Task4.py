



def my_all(iterable):
    for item in iterable:
        if not item:
            return False
    return True

def my_any(iterable):
    for item in iterable:
        if item:
            return True
    return False

def my_min(iterable):
    min_value = float('inf')
    for item in iterable:
        if item < min_value:
            min_value = item
    return min_value

def my_max(iterable):
    max_value = float('-inf')
    for item in iterable:
        if item > max_value:
            max_value = item
    return max_value

# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700
