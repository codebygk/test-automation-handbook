# Problem statement

# Given a string s, find the first character that appears exactly once in the string.

# If every character repeats, return None.

# Example 1

# Input: "leetcode"
# Output: "l"

def find_first_non_repeating_character(s: str):
    chars = list(s)
    count = {}
    for char in chars:
        count[char] = count.get(char, 0) + 1
    for char in chars:
        if count[char] == 1:
            return char
    return None

if __name__ == '__main__':
    print(find_first_non_repeating_character("leetcode"))  # l
    print(find_first_non_repeating_character("aabbcdd"))   # c
    print(find_first_non_repeating_character("aabbcc"))    # None