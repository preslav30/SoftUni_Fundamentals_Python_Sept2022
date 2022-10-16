def office(happiness_list, improvement_factor):
    multiply = [num * improvement_factor for num in happiness_list]
    great_happiness = [happy for happy in multiply if happy >= sum(multiply) / len(happiness_list)]
    if len(great_happiness) >= len(happiness_list) / 2:
        return f"Score: {len(great_happiness)}/{len(happiness_list)}. Employees are happy!"
    else:
        return f"Score: {len(great_happiness)}/{len(happiness_list)}. Employees are not happy!"


happiness = list(map(int, input().split()))
factor = int(input())
print(office(happiness, factor))
