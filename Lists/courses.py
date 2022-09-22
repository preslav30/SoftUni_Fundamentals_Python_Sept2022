def courses(number_of_courses):
    courses_list = []
    for courses in range(1, number_of_courses + 1):
        course = input()
        courses_list.append(course)
    return courses_list


print(courses(number_of_courses=int(input())))