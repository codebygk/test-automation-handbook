# Problem Statement

# Given a list of elements, find the element that appears most frequently.

# Example:

# nums = [1, 2, 3, 2, 4, 2, 5, 3]

# Output: 2

def find_most_frequent_element(nums: list):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    most_frequent = nums[0]
    for num in freq:
        if freq[num] > freq[most_frequent]:
            most_frequent = num
    return most_frequent

if __name__ == '__main__':
    nums = [1, 2, 3, 2, 4, 2, 5, 3]
    print(find_most_frequent_element(nums))