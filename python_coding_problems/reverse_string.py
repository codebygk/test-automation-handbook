# Problem statement

# Given a string s, reverse it without using Python's built-in reverse functions.

# Example:

# Input
# s = "hello"

# Output
# "olleh"

def reverse_string_using_loop(s: str):
    result = ''
    for char in s:
        result = char + result
    return result

def reverse_string_using_two_pointers(s: str):
    chars = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)

def reverse_string_using_slicing(s: str):
    return s[::-1]

if __name__ == '__main__':
    s = 'Hello'
    print(reverse_string_using_loop(s))
    # Use this in interviews
    print(reverse_string_using_two_pointers(s))
    # Built in function in python (fastest)
    print(reverse_string_using_slicing(s))