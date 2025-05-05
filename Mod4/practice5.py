'''5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. 
Ask the user for the order total and print the total cost, including shipping.
'''
total = float(input("What was your order total today? "))
shipping = float(5.00)
if total < 50:
    print(f"Your total is ${total:.2f}.")
else:
    total = total + shipping
    print(f"Your total is ${total:.2f}.")
