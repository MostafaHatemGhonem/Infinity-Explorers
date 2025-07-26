age=int(input("Enter your age please(your age must be between 10 and 100):"))
months=age*12
weeks=months*4
days=weeks*7
Hours=days*24
minuts=Hours*60
seconds=minuts*60
if age>=10 and age>=100:
    print(f"your age in months ={months}") 
    print(f"your age in weeks ={weeks}") 
    print(f"your age in days={days}") 
    print(f"your age in Hours ={Hours}") 
    print(f"your age in minuts={minuts}") 
    print(f"your age in seconds ={seconds}") 
else: 
    print("your age is not between 10 and 100")     
    