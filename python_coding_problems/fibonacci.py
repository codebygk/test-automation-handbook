# Problem Statement

# Given a non-negative integer n, generate the first n numbers of the Fibonacci sequence.

# The Fibonacci sequence starts with 0 and 1. Each subsequent number is the sum of the previous two numbers.

# Example 1

# Input:  n = 7

# Output: [0, 1, 1, 2, 3, 5, 8]

# Example 2

# Input:  n = 5

# Output: [0, 1, 1, 2, 3]


def fibonacci(n : int):
    result = []
    a = 0
    b = 1
    for _ in range(n):
        result.append(a)
        a,b = b, a + b
    return result


if __name__ == '__main__':
    print(fibonacci(2))
    print(fibonacci(5))
    print(fibonacci(10))