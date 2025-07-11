

try:
    email = input("Enter Your Email: ")
    email_parts = email.split('@')
    name = email_parts[0].capitalize()
    service_provider = email_parts[1].split('.')[0].lower()
    top_level_domain = email_parts[1].split('.')[1].lower()

    print(f"Your Name Is {name}")
    print(f"Email Service Provider Is {service_provider}")
    print(f"Top Level Domain Is {top_level_domain}")
except Exception as e:
    print(f"An error occurred: {e}")