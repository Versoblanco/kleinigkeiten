# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". (From: https://blog.codinghorror.com/why-cant-programmers-program/)

from multiple import multiple


def FizzBuzz(s=1, e=100):
    nums = list()
    for i in range(1, e +1):
        if multiple(i, 3) and multiple(i, 5):
            nums.append("FizzBuzz")
        elif multiple(i, 3):
            nums.append("Fizz")
            continue
        elif multiple(i, 5):
            nums.append("Buzz")
            continue
        else:
            nums.append(i)
    return nums


print FizzBuzz()
