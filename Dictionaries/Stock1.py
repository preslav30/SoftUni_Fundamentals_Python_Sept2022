products_and_quantities = input().split()
search_for = input().split()
products_dict = {products_and_quantities[key]: products_and_quantities[key + 1] for key in range(0, len(products_and_quantities), 2)}
for item in search_for:
    if item in products_dict.keys():
        print(f"We have {products_dict[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")