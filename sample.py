def call_counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print(f"Function '{func.__name__}' has been called {count} times")
        return func()

    return wrapper


# Example usage:
@call_counter
def my_function():
    print("Hello, world!")


my_function()
my_function()
my_function()
