students_dict = {}
while True:
    students_list = input().split(":")
    if len(students_list) == 1:
        final_course = "".join(students_list)
        break
    name = students_list[0]
    id = students_list[1]
    course = students_list[2]
    students_dict[name] = [id, course]
for key, value in students_dict.items():
    if value[1] == " ".join(final_course.split("_")):
        print(f"{key} - {value[0]}")