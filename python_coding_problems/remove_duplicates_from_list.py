# Problem statement

# Given a list of integers nums, remove all duplicate elements and return a new list containing only unique elements.

# Preserve the original order of the elements.

# Example 1

# Input:  [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

def remove_duplicates_from_list_using_loops(nums: list):
    unique_nums = []
    for n in nums:
        if n not in unique_nums:
            unique_nums.append(n)
    return unique_nums

def remove_duplicates_from_list_using_set(nums: list):
    unique_nums = set()
    for n in nums:
        unique_nums.add(n);
    return list(unique_nums)

if __name__ == '__main__':
    nums = [1, 2, 2, 3, 4, 4, 5]
    print(remove_duplicates_from_list_using_loops(nums))
    print(remove_duplicates_from_list_using_set(nums))