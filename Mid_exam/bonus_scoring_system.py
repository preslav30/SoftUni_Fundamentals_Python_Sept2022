import math

students = int(input())
lectures = int(input())
bonus = int(input())
max_bonus = 0
max_attendance = 0

for student in range(1, students + 1):
    attendance = int(input())
    total_bonus = attendance / lectures * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendance = attendance

print(f"Max Bonus: {math.ceil(max_bonus)}.\nThe student has attended {math.ceil(max_attendance)} lectures.")