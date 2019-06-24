# Input: string Output: string reversed (not sorted)
def reverse_str(my_str):
    """Take a string as input and returns a new string with the same characters in reversed order."""
    pos = len(my_str) - 1
    my_rev_str = ''
    while pos >= 0:
        my_rev_str += my_str[pos]
        pos -= 1
    return my_rev_str


# Test: should print roma
print reverse_str("amor")
