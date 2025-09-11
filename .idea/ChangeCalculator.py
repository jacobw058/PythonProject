num = float(input("enter an amount of money: "))
quarters = int(num / 0.25)
num %= 0.25
dimes = int(num / 0.1)
num %= 0.1
nickels = int(num / 0.05)
num %= 0.05
pennies = int(num * 100 + 0.5)
print("the minimum number of coins is:", (quarters + dimes + nickels + pennies))
print(quarters, "quarters", dimes, "dimes", nickels, "nickels", pennies, "pennies")