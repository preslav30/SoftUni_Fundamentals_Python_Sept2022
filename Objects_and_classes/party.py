class Party:

    def __init__(self):
        self.people = []


party = Party()
total = 0
while True:
    names = input()
    if names == "End":
        party.people = ", ".join(party.people)
        print(f"Going: {party.people}\nTotal: {total}")
        break
    else:
        party.people.append(names)
        total += 1


