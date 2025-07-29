# Write Function With Help To Get The Output

def say_hello_to(someone):
    """
    Function To Say Hello To Anyone
    parameter(someone) => Person Name
    """
    return f"Hello {someone}"

print(say_hello_to("Osama")) # "Hello Osama"

# Write Doc String Line For The Function Here

print(say_hello_to.__doc__)  # Output the docstring of the function

help(say_hello_to)  # Display the help information for the function

# Function Doc String Output