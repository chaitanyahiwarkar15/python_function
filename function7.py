#  Write a function that takes a list of numbers and returns the maximum number from the list.

def find_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num    
    return max_number
        
number_list = [10,25,789,65,485,52,54,475,5]
print("Maximum number ", find_max(number_list))

