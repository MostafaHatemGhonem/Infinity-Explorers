num=int(input("Please enter the number:")) 
count=0
if num> 0:
   while num > 0:
        print(num-1) 
        num-=1
        count+=1
        if num==7 or num==1:
           num-=1
   print(f"{count} numbers printed successfully!")    
else: 
    print(f"Number {num} is not larger than 0")    
