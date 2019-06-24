# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". (From: https://blog.codinghorror.com/why-cant-programmers-program/)

def multiple(num, mul):
    return num % mul == 0

def FizzBuzz():
    for i in range(1, 101):
        if multiple(i, 3) and multiple(i, 5):
            print "FizzBuzz"
            continue
        if multiple(i, 3):
            print "Fizz"
            continue
        if multiple(i, 5):
            print "Buzz"
            continue
        print i

# Write a loop that counts from 1 to 10

def count(start, end):
    for i in range(start, end+1):
        print i

count(1, 10)

# Write a loop that counts from 10 to 1

def reverse_count(start, end):
    while end <= start:
        print start
        start = start - 1

reverse_count(10, 1)


# Find smallest common multiple of two integers

def smallest_common_multiple(a, b):
    a, b = max(a, b), min(a, b)
    for i in range(a, a*b+1):
        if multiple(i, b) and multiple(i, a):
            return i

print smallest_common_multiple(3, 47)

# write a function that prints the nth Fibonacci number

# You have the numbers 123456789, in that order. Between each number, you must insert either nothing, a plus sign, or a multiplication sign, so that the resulting expression equals 2001. Write a program that prints all solutions. (There are two.) This is a pretty tricky problem, actually, if you don’t think to use recursion

# write a function that reverses a string
