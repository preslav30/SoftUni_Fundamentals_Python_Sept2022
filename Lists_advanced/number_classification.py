def number_classification(nums):
    pos = ", ".join(map(str, [posit for posit in nums if posit >= 0]))
    neg = ", ". join(map(str, [neg for neg in nums if neg < 0]))
    even = ", ". join(map(str, [ev for ev in nums if ev % 2 == 0]))
    odd = ", ". join(map(str, [od for od in nums if od % 2 != 0]))

    return f"Positive: {pos}\nNegative: {neg}\nEven: {even}\nOdd: {odd}"


numbers = list(map(int, input().split(", ")))
print(number_classification(numbers))
