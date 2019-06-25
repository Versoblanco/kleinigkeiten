"""Odds."""

# Write function to print the odd numbers from 1 to 99.


# def odd_nums(start, end):
#     """Return a list of odd numbers in a given range"""
#     odds = list()
#     for num in range(start, end + 1):
#         if num % 2 != 0:
#             odds.append(num)
#     return odds
def odd_nums(start, end):
    """Return a list of odd numbers in a given range."""
    odds = list(num for num in range(start, end + 1) if num % 2 != 0)
    return odds


print odd_nums(1, 99)
