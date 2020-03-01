#  Decorators are a way to dynamically alter the functionality of your functions. So for example, if you wanted to log information when a function is run, you could use a decorator to add this functionality without modifying the source code of your original function.


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper_function


# decorated_display = decorator_function(display)
# decorated_display()
# //with class


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print("Display function ran")


@decorator_class
def display_info(name, age):
    print("My name is {} and I am {} years old".format(name, age))


display()
display_info("Pramila", 25)
