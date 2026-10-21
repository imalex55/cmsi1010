# def blocks(n):
#     if n <= 0:
#         return 0
#     else:
#         return blocks(n - 1) + n

# print(blocks(8))
# print(blocks(0))
# print(blocks(-1))
# print(blocks(1))
# print(blocks(838852))

# One Liner Function: return ____ if ____ else ____
# raise TypeError("Input must be ___")

# Sum of digits: Write a recursive function sum_of_digits(n) that returns 
# the sum of the digits of a positive integer n. For example, sum_of_digits(1234) 
# should return 10.

def sum_of_digits(n):
    return n if n < 10 else sum_of_digits(n // 10) + (n % 10)

print(sum_of_digits(10939))

