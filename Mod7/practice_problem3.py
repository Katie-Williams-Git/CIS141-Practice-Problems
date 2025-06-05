'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
simple type effectiveness rules. Your solution only needs to work for these three sets of input:
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
'''

def type_advantage(attacker, defender):
    if attacker.lower() == "fire" and defender.lower() == "water":
        print("Not Very Effective")
    elif attacker.lower() == "water" and defender.lower()== "fire":
        print("Super Effective")
    else:
        attacker.lower() == "electric" and defender.lower() == "Grass"
        print("Neutral")


type_advantage("Water", "Fire")
type_advantage("Fire", "Water")
type_advantage("Electric", "Grass")
