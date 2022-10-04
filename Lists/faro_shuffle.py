def faro_shuffle(deck, number_of_shuffles):
    deck_list = deck.split(" ")
    middle = (len(deck_list)) // 2
    new_list = deck_list.copy()


    for shuffle in range(1, number_of_shuffles + 1):
        i = 0
        first_half = new_list[:middle]
        second_half = new_list[middle:]
        for j in range(len(first_half)):
            new_list[i] = first_half[j]
            new_list[i + 1] = second_half[j]
            j += 1
            i += 2


    print(new_list)


faro_shuffle(deck=input(), number_of_shuffles=int(input()))
