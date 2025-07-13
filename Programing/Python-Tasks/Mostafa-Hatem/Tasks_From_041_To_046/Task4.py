# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country: ")
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England", "Byala"]
price = 100
discount = 30

country = country.strip().title()

if country in countries:
    print(f"Your Country {country} Eligible For Discount And The Price After Discount Is: ${price - discount}")
else:
    print(f"Your Country {country} Not Eligible For Discount And The Price Is: ${price}")


# Needed Output
# "Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
# "Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example