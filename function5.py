# find max and min number 
# list[10,280,25,75,68,38,99,]
 
def mix_to_min(numbers):
    if not numbers:
        return none, none 
    max_val = numbers[0]
    min_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num 
        if num < min_val:
            min_val = num
    return max_val, min_val

numbers = [ 20,54,68,75,945,65,56,657,3,52]
max_value, min_value = mix_to_min(numbers)
print("sarvatjast Value ", max_value)
print("sarvat choti Value ", min_value)

