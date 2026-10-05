import math

n = int(input())

total_sum = sum(math.factorial(i) for i in range(1, n + 1))

print(total_sum)