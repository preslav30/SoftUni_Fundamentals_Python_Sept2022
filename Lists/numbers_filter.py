def numbers_filter(lines):
    nums = []
    new_list = []
    for line in range(1, lines + 1):
        num = int(input())
        nums.append(num)
    command = input()

    if command == "even":
        for number in nums:
            if number % 2 == 0:
                new_list.append(number)
    if command == "odd":
        for number in nums:
            if number % 2 != 0:
                new_list.append(number)

    if command == "negative":
        for number in nums:
            if number < 0:
                new_list.append(number)

    if command == "positive":
        for number in nums:
            if number >= 0:
                new_list.append(number)
    return new_list


print(numbers_filter(lines=int(input())))