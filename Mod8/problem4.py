'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas. Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''
import re


with open('poll.txt', 'r') as file:
    content = file.read().lower()
    words = re.findall(r"\b[\w']+\b", content)
    yea = 0
    nay = 0
    for word in words:
        if word == "yea":
            yea += 1
        elif word == "nay":
            nay += 1
    print(f"Yea = {yea},\nNay = {nay} ")
