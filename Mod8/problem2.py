'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

print("Welcome to the Hiking Trip Logger! This program updates a file named 'hiking_log' with trail names and distances in miles.")
print("Type '0' as the trail name to quit and see your log.\n")

# Dictionary to store hikes from this session
hike_log = {}

# Loop for user input
while True:
    trail = input("Enter trail name (or '0' to finish): ").strip()
    
    if trail == "0":
        break

    distance = input("Enter distance in miles: ").strip()

    try:
        distance = float(distance)
    except ValueError:
        print("Please enter a valid number for distance.")
        continue
    hike_log[trail] = distance

with open('hiking_log.txt', 'a') as file:
    for trail, distance in hike_log.items():
        file.write(f"{trail} - {distance} miles\n")

# Display contents of the log
print("\nYour updated hiking log:")
print("-------------------------")
try:
    with open('hiking_log.txt', 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Log file not found.")
