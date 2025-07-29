"""
Task 5: Rate Code By PyLint
"""

my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_people: list) -> None:
    """
    Function to greet a list of people.

    :param some_people: List of names to greet.
    :return: None
    """
    for person in some_people:
        print(f"Hello {person}")

say_hello(my_friends)
