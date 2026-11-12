def log_call(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        print(f'Positional arguments: {args}')
        print(f'keyword arguments: {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper