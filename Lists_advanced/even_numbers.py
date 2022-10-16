def even(nums):
    filtered = [nums.index(num) for num in nums if num % 2 == 0]
    return filtered


n = list(map(int, input().split(", ")))
print(even(n))
