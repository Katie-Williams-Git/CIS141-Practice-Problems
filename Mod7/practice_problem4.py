'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
(p.s if children are the driver's of a vehicle they get charged the adult rate)
'''
def ferry_fare(age, vehicle):
    int(age)
    vehicle = vehicle.lower()
    if age >= 19 and age <= 65  and vehicle == "yes":
        return "The fare is $20"
    elif age >= 19 and age <= 65 and vehicle == "no":
        return "The fare is $10"
    elif age >=64 and vehicle == "yes":
        return "The fare is $15"
    elif age >=64 and vehicle == "no":
        return "The fare is $5"
    elif age <= 18 and vehicle == "yes":
        return "The fare is $20."
    elif age <=18 and vehicle == "no":
        return "The fare is free."


test1 = ferry_fare(18, "No")
print(test1)
test2 = ferry_fare(21, "No")
print(test2)
test3 = ferry_fare(66, "Yes")
print(test3)
