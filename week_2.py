def find_sum(number):
    total = 0
    for num in number:
        total += num

    print(total)
nums = [1, 2, 3, 4]
find_sum(nums)

for num in range(1, 21):
    print(num)

maximum = float("-inf")
for num in nums:
    maximum = max(maximum, num)

print(maximum)