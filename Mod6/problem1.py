#1. Create a list of integers (you get to pick!). Write code to iterate through the list
#and calculate the sum of all even numbers. Print the resulting sum.
list = [5, 10, 15, 20, 25, 30, 35, 40]
alleven = list[1:8:2]
sumalleven = sum(alleven)
print(sumalleven)

#I came up with a different solution that would be more accurate for any numbers added to the list

list = [5, 10, 15, 20, 25, 30, 35, 40]
finalsum = 0
for iseven in list:
    if iseven % 2 == 0:
        finalsum += iseven
print(finalsum)
