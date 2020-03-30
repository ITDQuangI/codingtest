def decorate_answer(func):
    def inner(*args, **kwargs):
        print("#" * 10)
        print(func.__name__)
        func(*args, **kwargs)
        print("#" * 10 + "\n")
    return inner
