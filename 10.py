friends = ["Apple", "Banana", 5, False, "aadam"]

print(friends[0])

friends[0] = "Berries"      # lists are mutable(can be changed)

print(friends[0])
print(friends[0:2])


a = [1,5,9,2]
a.reverse()
a.pop(3)

a.insert(2, 333)
print(a)