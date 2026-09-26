def count_character_frequency(s: str):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == '__main__':
    s = 'banana'
    print(count_character_frequency(s))