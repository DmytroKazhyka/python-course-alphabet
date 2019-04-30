data = [x for x in range(0, 100)]

# print(any(data))
# print(all(data))

conditions = [True, True, {}, ]
print(all(conditions))

print(any(conditions))
print(bool([]))


new_data = []

if len(new_data) > 1:
    print("Not empty")
else:
    print("Empty")


if len(new_data) == True:
    print("Not empty")
else:
    print("Empty")


if new_data:
    print("Not empty")
else:
    print("Empty")

