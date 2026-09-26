# Problem Statement

# Given an integer n, determine whether it is a prime number.

# A prime number:

# is greater than 1
# has exactly two factors: 1 and itself

# Examples:

# 2  → Prime
# 3  → Prime
# 4  → Not Prime
# 7  → Prime
# 10 → Not Prime
# 1  → Not Prime

def check_prime_number(n: int):
    if n < 2:
        return False
    # Checking upto square root of the number is enough, since after that the factors just appear in reverse.
    # For example for 36 the factors are:
    # 1 x 36 = 36
    # 2 x 18 = 36
    # 3 x 12 = 36
    # 4 x 9  = 36
    # 6 x 6  = 36
    # 9 x 4  = 36
    # 12 x 3 = 36
    # 18 x 2 = 36
    # 36 x 1 = 36
    # Before and after 6 x 6 is the same.
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = 53
    print(check_prime_number(n))