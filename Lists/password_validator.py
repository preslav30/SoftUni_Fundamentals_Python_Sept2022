def validate(phrase):
    digit_counter = 0
    alnum = False
    count = False
    digits = False
    if phrase.isalnum():
        alnum = True
    else:
        print("Password must consist only of letters and digits")
    if 6 <= len(phrase) <= 10:
        count = True
    else:
        print("Password must be between 6 and 10 characters")
    for char in phrase:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
    else:
        digits = True
    if digits and count and alnum:
        print("Password is valid")


password = input()
validate(password)
