a = "A-1 A-5 A-10 B-2"
l = []
for t in a.split():
    try:
        l.append(float(t))
    except ValueError:
        pass

print(l)