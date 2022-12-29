lucky_number = [4, 5, 3, 9, 2]
friends = ["Terry", "Jim", "John", "Jack", "Tom"]
friends[1] = "Jhony"
friends.append("Tim")
friends.insert(4, "Colt")
friends.remove("Colt")
friends.sort()
friends.extend(lucky_number)
lucky_number.sort()
friends.pop()
print(friends)


friends2 = friends.copy()
print(friends2)
