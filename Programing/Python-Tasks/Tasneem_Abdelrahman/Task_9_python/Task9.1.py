num1=int(input("Please enter the first number: ").strip()) 
num2=int(input("Please enter the second number: ").strip()) 
operation=input("please enter the operator(+,-,/,*,%): ").strip()
if operation=="+": 
    print(num1+num2)
elif operation=="-": 
    print(num1-num2)    
elif operation=="*": 
    print(num1*num2)
elif operation=="/": 
    print (num1/num2)
elif operation=="%": 
    print(num1%num2)
else: 
    print("invalid operator") 