def get_random_number():
    print("Hi")
    yield 1
    print("Hello")
    yield 8
    print("Hero")
    yield 7777

generator = get_random_number()
print(next(generator))
print(next(generator))
print(next(generator))
