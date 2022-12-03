import time

def time_decorator(func):
    def wrapper():
        start_time = time.monotonic()
        result = func()
        print(f"{round((time.monotonic() - start_time))}")
        return result
    return wrapper

@time_decorator
def sleep_1_sec():
    time.sleep(3)
    print("function")
    return 25

result = sleep_1_sec()

print(result)
