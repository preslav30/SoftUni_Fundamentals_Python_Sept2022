def france(items_and_prices, budget):
    budget_copy = budget
    budget_after_selling = 0
    new_prices = []
    for item in items_and_prices:

        item = item.split("->")
        price = float(item[1])
        if item[0] == "Clothes" and price > 50:
            continue
        elif item[0] == "Shoes" and price > 35:
            continue
        elif item[0] == "Accessories" and price > 20.50:
            continue
        else:
            if budget > price:
                budget -= price
                item_sold = price * 1.4
                new_prices.append(item_sold)
                budget_after_selling += item_sold
            else:
                continue
    for item in new_prices:
        print(f"{item:.2f}", end=" ")

    diff = budget_copy - budget
    print(f"\nProfit: {budget_after_selling - diff:.2f}")

    if budget_after_selling + budget > 150:
        print("Hello, France!")
    else:
        print("Not enough money.")


france(items_and_prices=input().split("|"), budget=float(input()))