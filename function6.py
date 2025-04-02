#count even and odd in list 

def even_or_odd(numbers):
    results = []
    for num in numbers:
        if num % 2 == 0:
            print("This is a even number ", num)

        else:
            print("This is odd number ", num)
    return results

number_list = [10,25,48,36,13,71,69,37,9,12,14]
results = even_or_odd(number_list)
      