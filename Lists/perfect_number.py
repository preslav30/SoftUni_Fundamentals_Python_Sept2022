def perf(num):
    divisors = [x for x in range(1, num) if num % x == 0]
    if sum(divisors) == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."



the_int = int(input())
print(perf(the_int))