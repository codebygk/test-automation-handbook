# Problem Statement: Count Character Frequency

# Given a string s, write a Python function to count how many times each character appears in the string.

# Example:

# Input:
# s = "hello"

# Output:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def count_character_frequency(s: str):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == '__main__':
    s = 'banana'
    print(count_character_frequency(s))