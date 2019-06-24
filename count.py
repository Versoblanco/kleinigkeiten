"""Counting functions."""


# Write a loop that counts from 1 to 10
def countup(start, end):
    """."""
    count = ()
    for i in range(start, end+1):
        count += i,
    return count


print countup(1, 10)


# Write a loop that counts from 10 to 1
def countdown(start, end):
    """."""
    count = ()
    while end <= start:
        count += start,
        start = start - 1
    return count


print countdown(10, 1)
