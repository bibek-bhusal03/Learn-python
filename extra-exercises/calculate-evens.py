def count_evens(numbers): 
    count = 0
    for num in numbers:
        if(check_is_even(num)):
            count += 1
    return count


def check_is_even(number):
    return number % 2==0


number = [1, 2, 3, 4, 5, 6]

def calculate_number_of_evens():
    print(count_evens(number))




calculate_number_of_evens()