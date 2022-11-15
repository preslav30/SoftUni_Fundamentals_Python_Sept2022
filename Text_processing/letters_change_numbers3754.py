new_list = input().split()
text1 = ""
nums = []
processed_nums = []

for i in range(len(new_list)):
    num_str = ""
    for j in range(len(new_list[i])):
        if new_list[i][j].isdigit():
            num_str += new_list[i][j]
    nums.append(int(num_str))

    if new_list[i][0].isupper():
        result1 = nums[i] / (ord(new_list[i][0]) - 64)
    else:
        result1 = nums[i] * (ord(new_list[i][0]) - 96)
    if new_list[i][-1].isupper():
        result2 = result1 - (ord(new_list[i][-1]) - 64)
    else:
        result2 = result1 + (ord(new_list[i][-1]) - 96)
    processed_nums.append(result2)

print(f"{sum(processed_nums):.2f}")
