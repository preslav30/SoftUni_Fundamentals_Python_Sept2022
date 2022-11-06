products = {}
sum_all_quantities = 0

while True:
    pair = input()
    if pair == "statistics":
        break
    pair = pair.split(": ")
    item = pair[0]
    quantity = int(pair[1])
    if item in products.keys():
        products[item] += quantity
    else:
        products.update({item: quantity})
for value in products.values():
    sum_all_quantities += value
print(f"Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}\nTotal Quantity: {sum_all_quantities}")
