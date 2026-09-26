# Problem statement

# Given two strings s and t, determine whether they are anagrams of each other.

# An anagram is a word formed by rearranging the letters of another word, using every letter exactly the same number of times.

# Example 1:

# Input:
# s = "listen"
# t = "silent"

# Output: True

# Example 2:

# Input:
# s = "rat"
# t = "car"

# Output: False

def is_anagram(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    for char in s1:
        if char not in s2:
            return False
        # Replaces first occurrence of a character in a string and assigns back to the variable.
        s2 = s2.replace(char, "", 1)
    return True


if __name__ == '__main__':
    s1 = 'listen'
    s2 = 'silent'
    print(is_anagram(s1, s2))
    s3 = 'rat'
    s4 = 'car'
    print(is_anagram(s3, s4))