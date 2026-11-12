'''
LESSON 02 - DECORATOR
decorator
@ to call
*args and **kwargs
'''
import time
import practice

def time_it(func):
    def func_with_timing(*args, **kwargs):
        start_time = time.time()
        print(start_time)
        result = func(*args, **kwargs)
        end_time = time.time()
        print(end_time)
        duration = end_time - start_time
        print(f'Function {func.__name__} executed in {duration:.8f} seconds')
        return result
    return func_with_timing

@time_it
def square_list_creator():
    return [x**2 for x in range(100000)]

@time_it
def square_list_creator1(n):
    return [x**2 for x in range(n)]

@time_it
def square_list_creator2(num, **options):
    return [x**2 for x in range(num) if options['threshold'] > x and x % options['offset'] == 0]

@practice.log_call
def make_profile(name, **details):
    profile = {"name": name}
    profile.update(details)
    return profile

def main():
    #square_list_creator()
    #square_list_creator1(200000)
    #square_list_creator2(300000, threshold = 100, offset = 10)
    profile = make_profile("Maya", age = 25, city = "harare")
    print(profile)


if __name__ == '__main__':
    main()