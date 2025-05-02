'''#4. Prompt the user for: a word, a first index, and a last index.
Slice the word at the indexes provided by the user and print to the screen.
'''
word = input("Please enter a word.")

wordlength = len(word)
print(f"Your word was {wordlength} characters long. Please prepare to enter two numbers between 0 and {wordlength}.")

index1 = int(input("Please enter a number."))

index2 = int(input("Please enter a number bigger than your first one."))

sliceone = word[index1:index2]
print(sliceone)
