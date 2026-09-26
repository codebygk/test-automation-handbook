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
    return True


if __name__ == '__main__':
    s1 = 'listen'
    s2 = 'silene'
    print(is_anagram(s1, s2))
