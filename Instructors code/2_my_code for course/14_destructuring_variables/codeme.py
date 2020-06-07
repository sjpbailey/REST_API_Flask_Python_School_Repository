#x, y = 5, 11

# x, y = (5, 11)

# -- Destructuring in for loops --

#student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

#print(list(student_attendance.items()))

#for student, attendance in student_attendance.items():
    
#   print(f"{student}: {attendance}")

# -- Another example --

#people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

#for name, age, profession in people:
#    print(f"Name: {name}, Age: {age}, Profession: {profession}")

#for person in people:
#    print(f"name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

# -- Ignoring values with underscore --

person = ("Bob", 42, "Mechanic")
name, _, profession = person #or just name, profession = person

print(name, profession)  # Bob Mechanic
