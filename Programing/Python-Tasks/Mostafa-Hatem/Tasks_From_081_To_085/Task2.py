
# Create Your Decorator Here

def sugar_decorator(func):
    def wrapper(*args, **kwargs):
        print("Sugar Added From Decorators")
        result = func(*args, **kwargs)
        print("####################")
        return result
    return wrapper

@sugar_decorator
def make_tea():
  print("Tea Created")
@sugar_decorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()
