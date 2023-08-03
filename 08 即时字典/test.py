def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function is called.")
        result = func(*args, **kwargs)
        print("After function is called.")
        return result

    return wrapper


@my_decorator
def my_function():
    print("Function is called.")


my_function()
