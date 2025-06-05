#1. Write a function called count_vowels(input) that takes a string
#and returns the number of vowels (a, e, i, o, u) in it.
'''
def count_vowels(input):
    vowel = "aeiou"
    count = 0
    for letter in input:
        if letter.lower() in vowel:
            count += 1
    return count


count1 = "something"
result = count_vowels(input = count1)
print(result)

count2 = "somethiiiiing"
result2 = count_vowels(input = count2)
print(result2)
