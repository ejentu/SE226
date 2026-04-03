def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


abs_x = lambda x, i: (x ** (2 * i)) / factorial(2 * i)


def exp_x(x_, n_):
    summation = 0
    for i in range(n_):
        summation += (-1) ** i * abs_x(x_, i)
    return summation


x = int(input("Enter x : "))
n = int(input("Enter n : "))
print(exp_x(x, n))

sayi = 0


def show_logic(n, r):
    """
    this function works recursively
    it starts from n and goes until it reaches 0
    at every step we add the r**n to the 'sayi' variable
    when n == 0, r**0 == 1 so it stops.
    when n is negative it can't pass the 'if' therefore no iterations occur.
    """
    global sayi
    if n < 0:
        return
    sayi += r ** n
    show_logic(n - 1, r)



show_logic(3,4)
print(sayi)

