def loading(num):
    percent_signs = num // 10
    if num == 100:
        print("100% Complete!\n[%%%%%%%%%%]")
    else:
        print(f"{num}% [{percent_signs * '%'}{(10 - percent_signs) * '.'}]")
        print("Still loading...")


n = int(input())
loading(n)
