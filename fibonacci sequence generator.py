
#define your fib fuction
#assign your fisrt 2 consecutive numbers to start with
# using an if statement construct the pattern of a sequence
#with a for loop define the successive numbers in your sequence
#call your function for the first n fibonucci numbers of choice
def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    elif n <= 0:
        print("invalid input, n must be greater than 0")
    # elif n >= 100:

    else:
        print(a)
        print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


fib(100)