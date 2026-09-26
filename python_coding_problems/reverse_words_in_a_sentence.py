# Problem statement

# Given a sentence, reverse the order of the words without reversing the characters inside each word.

# Remove any leading or trailing spaces and replace multiple spaces between words with a single space.

# Example:

# Input: I Love Python

# Output: Python Love I

def reverse_words_in_a_sentence(s: str):
    s = s.split()
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ' '.join(s)

if __name__ == '__main__':
    s = 'I Love Python'
    print(reverse_words_in_a_sentence(s))