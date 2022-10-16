def electrons(number_of_electrons):
    shell_position = 1
    el_list = []
    while True:
        max_el = 2 * (shell_position ** 2)
        if number_of_electrons >= max_el:
            number_of_electrons -= max_el
            el_list.append(max_el)

        else:
            remainder = number_of_electrons
            el_list.append(remainder)
            break
        if number_of_electrons <= 0:
            break
        else:
            shell_position += 1
    return el_list


el = int(input())
print(electrons(el))
