companies = {}
while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split(" -> ")
    if company_name in companies.keys():
        if employee_id in companies[company_name]:
            continue
        else:
            companies[company_name].append(employee_id)
    else:
        companies[company_name] = [employee_id]


for company in companies.keys():
    print(f"{company}")
    for ids in range(len(companies[company])):
        print(f"-- {companies[company][ids]}")
