def count_numbers(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count

print(count_numbers("hello@123"))  
