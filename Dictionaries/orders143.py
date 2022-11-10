final_dict = {}
while True:
    command = input().split()
    if len(command) == 1:
        break
    name = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if name in final_dict:
        final_dict[name][0] = price
        final_dict[name][1] += quantity
    else:
        final_dict[name] = [price, quantity]

for product_name, price1 in final_dict.items():
    total_price = final_dict[product_name][0] * final_dict[product_name][1]
    print(f"{product_name} -> {total_price:.2f}")
