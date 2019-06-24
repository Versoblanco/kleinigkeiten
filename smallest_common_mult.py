"""Find smallest common multiple of two integers"""

from multiple import multiple

def smallest_common_multiple(a, b):
    a, b = max(a, b), min(a, b)
    for i in range(a, a*b+1):
        if multiple(i, b) and multiple(i, a):
            return i

print smallest_common_multiple(3, 47)
