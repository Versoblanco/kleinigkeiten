# -*- coding: utf-8 -*-
"""Fibonacci functions."""
# Fibonacci F(n) = {0, 1, 1, 2, 3, 5, ..., f(n)} for n>1 F(n) = F(n-1) + F(n-2)

###########################################################
#  Write a function that prints the nth Fibonacci number  #
###########################################################


# Fibonacci with tree recursion, exponential growth
def fib_tree(n):
    if n == 0 or n == 1:
        return n
    return fib_tree(n-1) + fib_tree(n-2)


# Fibonacci with iterative recursion using a <for> loop
def fib_loop(n):
    if n == 0 or n == 1:
        return n
    a, b = 1, 0
    for i in range(2, n+1):
        f = a + b
        a, b = f, a
    return f


# Same iterative recursion without explicit <for> loop
def fib_iter(n, i = 2, a = 1, b = 0):
    if n == 0 or n == 1:
        return n
    f = a + b
    a, b = f, a
    i += 1
    if i > n:
        return f
    return fib_iter(n, i, a, b)


# Fibonacci dictionary. It can be stored and get later all the n-keys needed values at once.
def fib_dict(n):
    """Return fibonacci dictionary with n-keys and f(n)-values within range {0: 0, ..., n: f(n)}."""
    f = {0 : 0, 1 : 1}
    if n == 0 or n == 1:
        return n
    for i in range(2, n+1):
        f[i] = f.get(i, f[i-1] + f[i-2])
    return f

################################################################
#  Write a function that prints n of a given Fibonacci number  #
################################################################

def find_nth(fib):
    if fib == 0:
        return 0
    if fib == 1:
        return 1, 2
    n = 3
    while fib_loop(n) != fib:
        n += 1
    return n


########################################################
#  Test nth(0, 1, 2, 15, 18), Fib(0, 1, 1, 610, 2584)  #
########################################################

print "Fibonacci of ", find_nth(0), find_nth(1), find_nth(2), find_nth(610), find_nth(2584), find_nth(259695496911122585)
print(fib_loop(0), fib_loop(1), fib_loop(2), fib_loop(15), fib_loop(18), fib_loop(85))
fdict = fib_dict(85)
print(fdict.get(0), fdict.get(2), fdict.get(1), fdict.get(15), fdict.get(18), fdict.get(85))
print(fib_iter(0), fib_iter(1), fib_iter(2), fib_iter(15), fib_iter(18), fib_iter(85))


# Only with low numbers!
print(fib_tree(0), fib_tree(1), fib_tree(2), fib_tree(15), fib_tree(18))
