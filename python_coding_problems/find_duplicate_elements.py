# Problem statement

# Given a list of integers, find all elements that appear more than once.

# Return each duplicate only once.

# Example 1

# Input:  [1, 2, 3, 2, 4, 5, 3]

# Output: [2, 3]

# Example 2

# Input:  [1, 2, 3, 4]

# Output: []

def find_duplicate_elements(nums: list):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

if __name__ == '__main__':
    nums1 = [1, 2, 3, 2, 4, 5, 3]
    nums2 = [1, 2, 3, 4]
    print(find_duplicate_elements(nums1))
    print(find_duplicate_elements(nums2))