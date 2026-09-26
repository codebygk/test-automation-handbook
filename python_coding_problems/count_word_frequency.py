# Problem statement

# Given a sentence, count how many times each word appears.

# Return a dictionary where:

# word → frequency
# Example
# s = "python is easy and python is powerful"

# Expected output:

# {
#     "python": 2,
#     "is": 2,
#     "easy": 1,
#     "and": 1,
#     "powerful": 1
# }

def count_word_frequency(s: str):
    seen = {}
    words = s.split()
    for word in words:
        seen[word] = seen.get(word, 0) + 1
    return seen


if __name__ == '__main__':
    s = 'python is easy and python is powerful'
    print(count_word_frequency(s))