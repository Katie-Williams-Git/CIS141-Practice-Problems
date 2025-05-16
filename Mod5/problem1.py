#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. 
#Print the final sum.

n = int(input("Please give me a positive whole number. "))
start = 1
while start <= n:
    print(start)
    start+=1
    if start == n + 1:
        break
    
