'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console



#Collect user input to find 5 words
word_input = input("Please enter 5 words you would like to search for in song_lyrics, separated by commas like 'Night, tears, pain, crying, no': ").strip().lower()
#put into a list so multiple values can be searched
word_list = [word.strip() for word in word_input.split(",")]
#pull open the file
with open('song_lyrics.txt', 'r') as file:
    content = file.read().lower()
#create dictionary to be printed
count_dict = {}
#make function to add to dictionary
def add_count(count_dic, word, content):
    amount = content.count(word)
    count_dic[word] = amount
#use function on user input
for word in word_list:
    add_count(count_dict, word, content)

# Count each word
for word in word_list:
    amount = content.count(word)
    count_dict[word] = amount

# Print the results
print("\nWord counts in song_lyrics.txt:")
for word, count in count_dict.items():
    print(f"'{word}' appears {count} time(s). ")

'''
#alternate version that's slightly more accurate

#create a dictionary to be printed
count_dict = {}
#create a function to add to the dictionary
def add_count(count_dict, word, content):
    word_count = content.split().count(word)
    if word in count_dict:
        count_dict[word] += word_count
    else:
        count_dict[word] = word_count
#import module re (recognized expression?) to help with formatting
import re
#bring in file with workable variable name
with open('song_lyrics.txt', 'r') as file:
        content = file.read().lower()
        words = re.findall(r"\b[\w']+\b", content)

# Get user input
dict_words = input("Please enter 5 words you would like to search for in song_lyrics, separated by a comma like 'Night, tears, pain, crying, no': ")
count_list = [word.strip().lower() for word in dict_words.split(",")]

# Count each word using the function
for word in count_list:
    add_count(count_dict, word, content)

counts = {word: words.count(word) for word in count_list}

# Print results
print("\nSearch Results:")
for word, count in counts.items():
    print(f"'{word}' appears {count} time(s)")

'''

song_url = https://youtu.be/6zTYTnyvk7k
'''
