num = int(input("enter value in fahrenheit: "))
temp = num
num -= 32
num /= 9
num *= 5
num += 0.5
print(temp, "degrees fahrenheit is", int(num), "degrees celsius")