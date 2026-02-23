n = int(input("Enter vale of n: "))
factorial = 1

while n>0:
    # factorial = factorial * n
    # n = n -1
    factorial *=n
    n -= 1
print("Factorial: ", factorial)