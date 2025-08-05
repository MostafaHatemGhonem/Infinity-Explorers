def addition(*numbers): 
    result=0
    for number in numbers: 
        if number==10:
             continue
        elif number==5:
             result-=number 
        else: 
             result+=number
    return result 
print(addition(10,20,30,40,5)) 
    