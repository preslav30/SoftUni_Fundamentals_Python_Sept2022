def even(nums):
    filtered = [i for i, num in enumerate(nums) if num % 2 == 0]
    return filtered


n = list(map(int, input().split(", ")))
print(even(n))
