hearts = list(map(int, input().split("@")))
the_end = False
index = 0
failed = 0
all_done = True
command = input()
while command != "Love!":
    command = command.split()
    jump = int(command[1])
    index += jump
    if index > len(hearts) - 1:
        index = 0
    if hearts[index] == 0:
        print(f"Place {index} already had Valentine's day.")
        command = input()
        continue
    hearts[index] -= 2
    if hearts[index] == 0:
        print(f"Place {index} has Valentine's day.")
    command = input()

for house in range(len(hearts)):
    if hearts[house] != 0:
        failed += 1
        all_done = False


print(f"Cupid's last position was {index}.")
if all_done:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")