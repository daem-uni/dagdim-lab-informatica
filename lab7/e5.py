import random

nums = []

for i in range(20):
    nums.append(random.randint(0, 100))

for n in nums:
    print(n, end=" ")
print()

nums = sorted(nums)

for n in nums:
    print(n, end=" ")
print()
