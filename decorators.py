# Define a decorator class
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        result = self.func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

# Use the decorator class to modify a function
@MyDecorator
def say_hello(name):
    print(f"Hello, {name}!")

# Call the decorated function
say_hello("Alice")
