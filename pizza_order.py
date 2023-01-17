print("Welcome to the Vamshi pizza!")

v = input("which size pizza would you like to order S, M, L? ")

if v == "S":
    bill = 10
elif v == "M":
    bill = 15
elif v == "L":
    bill = 20

p = input("do you want pepperoni? (y/n) ")

if p == "y":
 bill += 5

c = input("would you like cheese? (y/n) ")
if c == "y":
    bill+=5


print(f"your final bill is {bill}")
