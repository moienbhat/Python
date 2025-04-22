lucky_numbers = [4, 8, 15, 16]

friends = ["Kevin", "Karen", "Kim"]
print(friends[0])
print(friends[-2])
print(friends[0:2])

friends.extend(lucky_numbers)
print(friends)
friends.append("Jim")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)
print(friends.index("Kevin"))

print(friends.index("Melvin"))

friends.sort()
print(friends)     #ascending order

friends.reverse()
print(friends)

friends2 = friends.copy()
print(friends)







