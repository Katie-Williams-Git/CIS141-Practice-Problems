#4.  Create a list of integers. Write code that counts how many numbers are positive and how many are negative, 
#then print both counts.

my_list = [-3,-2,-1,0,1,2,3]
positiv = 0
negativ = 0

for i in my_list:
    if i >0:
        positiv += 1
    elif i < 0:
        negativ += 1
    
print(positiv)
print(negativ)
