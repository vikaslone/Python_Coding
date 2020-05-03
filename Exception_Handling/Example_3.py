"""

Write a function that asks for an integer and prints the square of it.
Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    pass
In [4]:
ask()
Input an integer: null
An error occurred! Please try again!
Input an integer: 2
Thank you, your number squared is:  4

"""


def square():
    while True:
        try:
            num1 = int(input('Enter an integer: '))
        except:
            print('Enter an integer to perform an operation')
            continue
        else:
            break

    print(num1**2)


square()