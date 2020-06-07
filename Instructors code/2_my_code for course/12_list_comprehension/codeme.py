#numbers = [1, 3, 5]
#squares = [x * 2 for x in numbers]

#for num in numbers:
#    doubled.append(num * 2)
#print(squares)

# -- Dealing with strings --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
#starts_s = [friend for friend in friends if friend.startswith("S")]
starts_s = friends

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), " starts_s: ", id(starts_s))


#for friend in friends:
#    if friend.startswith("S"):
#        starts_s.append(friend)

