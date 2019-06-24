# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". (From: https://blog.codinghorror.com/why-cant-programmers-program/)

from multiple import multiple


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
