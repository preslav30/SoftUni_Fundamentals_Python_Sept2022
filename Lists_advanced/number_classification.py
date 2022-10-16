def number_classification(nums):
    pos = [posit for posit in nums if posit >= 0]
    neg = [neg for neg in nums if neg < 0]
    even = [ev for ev in nums if ev % 2 == 0]
    odd = [od for od in nums if od % 2 != 0]

    return f"Positive: {pos}\nNegative: {neg}\nEven: {even}\nOdd: {odd}"


numbers = list(map(int, input().split(", ")))
print(number_classification(numbers))
