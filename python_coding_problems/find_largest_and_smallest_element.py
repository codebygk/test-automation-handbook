# Problem statement

# Given a list of integers, find the largest and smallest elements without using Python's built-in max() and min() functions.

# Example
# nums = [5, 2, 9, 1, 7]

# Output:

# Smallest: 1
# Largest: 9

def find_largest_and_smallest_element(nums: list):
    smallest = nums[0]
    largest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

if __name__ == '__main__':
    nums = [5, 2, 9, 1, 7]
    smallest, largest = find_largest_and_smallest_element(nums)
    print(f'Smallest: {smallest}')
    print(f'Largest: {largest}')