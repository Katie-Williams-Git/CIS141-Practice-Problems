#2. Create a list of strings. Write code that counts how many times the word "Olympic" appears in the list, 
#and then print the count.

strings = ["bear", "runs", "down", "the", "highway", "at", "olympic", "college.", "which", "is", "on", "the", "Olympic", "Peninusla"]
word = "olympic"
count = 0
for comp in strings:
    if comp.lower() == word:
        count += 1
print(count)
