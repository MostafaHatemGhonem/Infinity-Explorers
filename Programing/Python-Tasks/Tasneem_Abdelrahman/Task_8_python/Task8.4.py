email=input("Please enter your email: ")
email=email.lower() 
name=email[:email.index("@")]
name=name.strip().capitalize()
website=email[email.index("@")+1:email.index(".")]
website=website.strip().capitalize()
Domain=email[email.index(".")+1:]
print(f"Your name is {name}") 
print(f"Email service provider is {website}")
print(f"Top level domain is {Domain}")