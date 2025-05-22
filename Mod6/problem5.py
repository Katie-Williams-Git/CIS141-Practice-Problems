#5. Create a list of integers. Use a loop to build a new list where each element is the square of the corresponding 
#element in the original list. Print the new list.# Write your code here :-)


ints = [1,2,3,4,5]
squares = []
for inde in ints:
    #print(ints.index(inde))
    item = pow(inde, 2)
    squares.append(item)
print(squares)
