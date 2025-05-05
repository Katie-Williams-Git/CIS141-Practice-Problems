'''4. A theater wants to enforce age restrictions for movie tickets. 
Ask the user for their age, and tell them whether they can see G (appropriate for under 13), 
PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
'''
age = int(input("What is your age? "))
if age < 13:
    print("You may watch any G rated movie.")
elif age < 18:
    print("You may watch PG-13 or G rated movies.")
else:
    print("You may watch R, PG-13, or G rated movies.")
