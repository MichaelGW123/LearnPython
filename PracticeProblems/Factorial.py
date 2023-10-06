# Michael Williamson
# Factorial
# 7/23/2020

number = input("What number would you like the factorial of? ")


def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)


if number == "0":
    print("The factorial of " + number + " is 1")
elif int(number) < 0:
    print("Negative numbers do not have factorials")
else:
    print("The factorial of " + number + " is " + str(factorial(int(number))))
