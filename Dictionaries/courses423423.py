registered = {}
while True:
    command = input()
    if command == "end":
        break
    command = command.split(" : ")
    course_name = command[0]
    student_name = command[1]
    if course_name in registered.keys():
        registered[course_name].append(student_name)
    else:
        registered[course_name] = [student_name]
# for course, names in registered.items():
for courseee, nameee in registered.items():
    print(f"{courseee}: {len(registered[courseee])}")
    for j in range(len(registered[courseee])):
        print(f"-- {registered[courseee][j]}")