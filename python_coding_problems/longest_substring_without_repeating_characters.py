# Problem Statement

# Given a string, find the length of the longest substring that contains no repeating characters.

# A substring must be contiguous.

# Examples:

# Input:  "abcabcbb"
# Output: 3

def longest_substring_without_repeating_characters(s: str):
    max_length = 0
    seen = set()
    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == '__main__':
    s = 'abcabcbb'
    print(longest_substring_without_repeating_characters(s))