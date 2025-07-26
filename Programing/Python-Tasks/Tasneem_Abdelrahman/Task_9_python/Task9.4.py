country = input("Please enter Your Country:").strip().capitalize() 
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print("Your Country Eligible For Discount And The Price After Discount Is $70") 
else:
    print("Your Country Not Eligible For Discount And The Price Is $100") 
    