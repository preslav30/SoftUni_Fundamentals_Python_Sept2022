import json

# initialising dictionary
test1 = {"testname": "akshat",
         "test2name": "manjeet",
         "test3name": "nikhil"}

# print original dictionary
print(type(test1))
print("initial dictionary = ", test1)

# convert dictionary into string
# using json.dumps()
result = json.dumps(test1)

# printing result as string
print("\n", type(result))
print("final string = ", result)