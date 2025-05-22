#3. Create a list of strings. Write code to create a new list that includes only the strings longer than three characters. 
#Print the resulting filtered list.

strings = ["the", "apple", "orange", "key", "random", "internet", "stuff", "I", "am"]
size = 3
longstrings = []#I'm trying to make this a new list with words from strings that are longer than 3 characters
for i in strings:
    if len(i) > size:
        longstrings.append(i)
print(longstrings)
