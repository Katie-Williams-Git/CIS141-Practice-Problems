#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. 
#Print the final sum.
'''
n = int(input("Please give me a positive whole number. "))
start = 1
while start <= n:
    print(start)
    start+=1
    if start == n + 1:
        break
#This code doesn't solve the problem but I have kept it in purely for the record.
'''
#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n.
#Print the final sum.

n = int(input("Please give me a positive whole number. "))
start = 0
finalsum = 0
while start < n:
    start += 1
    finalsum += start
print(finalsum)
