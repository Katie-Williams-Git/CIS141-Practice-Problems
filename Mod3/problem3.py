'''#3. Prompt the user for a sentence and a word to try to find in that sentence. 
Have the program print out whether the word was found in the sentence. (i.e. True or False)
'''
sent = input("Please enter a sentence. ")
word = input("Enter any word to have the computer search the sentence for it. ")
look = word in sent
print("Was it there? ", look)
