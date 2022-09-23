str_of_ints = "3, 4, 5, 1, 29, 4"
new_list = []
# new_list = str_of_ints.split(", ")   # ['3', '4', '5', '1', '29', '4']


for num in str_of_ints.split(", "):
    new_list.append(int(num))

print(new_list)
