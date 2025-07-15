num_1= int(input("enter your number"))
operation=input("enter your operation'+' '-' '*' '/'")
num_2=int(input("enter your number"))
if operation== "+" :
   result= num_1 + num_2
elif operation=="-" :
      result= num_1 - num_2
elif operation=="/" :
    if num_2!=0 :
         rusult= num_1 / num_2
    else:
        result= "what\'s rong!"
elif operation=="*" :
      result= num_1 * num_2
else :

    print("rong of operation!")
