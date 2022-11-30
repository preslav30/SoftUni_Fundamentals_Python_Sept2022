sample_list = [1, 1, 8, 4, 4, 2, 4, 8]
print(f"Original list {sample_list}")

occurrences = {}
for n in sample_list:
    occurrences[n] = sample_list.count(n)
print(occurrences)

# Original list  [1, 1, 8, 4, 4, 2, 4, 8]
# Printing count of each item   {1: 2, 8: 2, 4: 3, 2: 1}