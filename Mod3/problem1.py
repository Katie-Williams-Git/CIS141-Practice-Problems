'''1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. 
Use the skills you learned in this module to print the word the correct number of times.'''
word = input("Please enter a word. ")
repeat = int(input("How many times would you like to see that word repeated? Please pick a number between 1-1,000: "))
display = word * repeat
print(display)
