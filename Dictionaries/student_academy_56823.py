rows = int(input())
grades_dict = {}
final_dict = {}
for row in range(rows):
    name = input()
    grade = float(input())
    if name in grades_dict.keys():
        grades_dict[name].append(grade)
    else:
        grades_dict[name] = [grade]

for names, grades in grades_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f"{names} -> {average_grade:.2f}")