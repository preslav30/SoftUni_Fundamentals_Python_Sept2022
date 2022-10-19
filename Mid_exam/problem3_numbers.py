numbers = list(map(int, input().split()))
avg_value = sum(numbers) / len(numbers)
list_of_top_five = []

for i in range(len(numbers) - 1, - 1, - 1):
    if numbers[i] <= avg_value:
        numbers.remove(numbers[i])
if len(numbers) == 0:
    print("No")
    quit()
elif len(numbers) > 5:
    while len(numbers) > 5:
        numbers.remove(min(numbers))

numbers.sort(reverse=True)

for num in range(len(numbers)):
    numbers[num] = str(numbers[num])
result = " ".join(numbers)
print(result)
