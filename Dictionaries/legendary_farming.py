not_junk = ["shards", "fragments", "motes"]
junk = {}
command_dict = {}
obtained = False
while True:
    command = input().lower().split()
    for key1 in range(0, len(command), 2):
        material = command[key1 + 1]
        amount = int(command[key1])
        if material in not_junk:
            if material in command_dict:
                command_dict[material] += amount
            else:
                command_dict[material] = amount
            if command_dict[material] >= 250:
                if material == "shards":
                    legendary = "Shadowmourne"
                elif material == "fragments":
                    legendary = "Valanyr"
                elif material == "motes":
                    legendary = "Dragonwrath"
                print(f"{legendary} obtained!")
                command_dict[material] -= 250
                obtained = True
                break

        else:
            if material in junk:
                junk[material] += amount
            else:
                junk[material] = amount
    if obtained:
        break
if "shards" in command_dict.keys():
    shards = command_dict["shards"]
else:
    shards = 0
if "fragments" in command_dict.keys():
    fragments = command_dict["fragments"]
else:
    fragments = 0
if "motes" in command_dict.keys():
    motes = command_dict["motes"]
else:
    motes = 0
print(f"shards: {shards}")
print(f"fragments: {fragments}")
print(f"motes: {motes}")

for junk_key, junk_value in junk.items():
    print(f"{junk_key.lower()}: {junk_value}")
