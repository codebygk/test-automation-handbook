# Problem statement

# Given a string s, determine whether it is a palindrome.

# A palindrome is a string that reads the same forward and backward.

# Examples:

# Input:  "madam"
# Output: True

# Input:  "hello"
# Output: False

def check_palindrome(s: str):
    chars = list(s)
    left = 0
    right = len(chars) - 1
    while left < right:
        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    s1 = 'madam'
    s2 = 'doctor'
    print(check_palindrome(s1))
    print(check_palindrome(s2))