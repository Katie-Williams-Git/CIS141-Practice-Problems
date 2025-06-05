
'''
#5. Write a function called level_up(experience) that takes a player's experience
points and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''

def level_up(experience):
    if experience >= 0 and experience <=99:
        return "Level 1"
    elif experience >= 100 and experience <=199:
        return "Level 2"
    elif experience >= 200:
        return "Level 3"
    else:
        return ""

test1 = 25
print(level_up(test1))
test2 = 100
print(level_up(test2))
test3 = 200
print(level_up(test3))
test4 = -2
print(level_up(test4))
