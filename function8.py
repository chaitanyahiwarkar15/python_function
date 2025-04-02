# Write a function count_vowels(text) that counts the number of vowels (a, e, i, o, u) in a given string.

def count_vowels(text):
    vowels ='aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

sentence = "Hello this is chaitanya , I am data analyst"
print("Vowels count ", count_vowels(sentence))