
def print_something(first_value):
    print(f"Starting the search for {first_value}")
    while True:
        name = (yield)
        if first_value in name:
            print(f"success, you are a awesome: {name}")
        else:
            print(f"{name} did not match")



corou = print_something('you')
corou.__next__()
corou.send('you')
corou.send('nice you')
