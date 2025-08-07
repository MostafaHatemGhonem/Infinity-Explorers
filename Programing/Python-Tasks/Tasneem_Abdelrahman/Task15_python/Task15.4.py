def my_all (iterable): 
    for value in iterable: 
        if bool(value)==False: 
             return False
    return True         
    
    
def my_any(iterable): 
    for value in iterable: 
        if bool(value): 
            return True
    return False 
    
    
def my_min (values):
    min_value=values[0]
    if values: 
       for value in values: 
           if value<min_value: 
              min_value=value
       return min_value      
    else:
         return None   
       
def my_max(items):  
     max_item=items[0]
     if items: 
        for item in items: 
            if item>max_item:
               max_item=item
        return max_item      
     else:
         return None     


print(my_all([1, 2, 3])) 
print(my_all([1, 2, 3, []])) 
print(my_any([0, 1, [], False])) 
print(my_any([(), 0, False])) 
print(my_min([10, 100, -20, -100, 50])) 
print(my_max((10, 100, -20, -100, 50, 700))) 