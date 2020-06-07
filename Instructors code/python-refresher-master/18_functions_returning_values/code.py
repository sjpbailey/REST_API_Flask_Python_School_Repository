#def add(x, y):
 #   print(x + y)


#add(5, 8)
#result = add(5, 8)
#print(result)  # None

# If we want to get something back from the function, it must return a value.
# All functions return _something_. By default, it's None.

# -- Returning values --


#def add(x, y):
#    return x + y


#add(1, 2)  # Nothing printed out anymore.
#result = add(2, 3)
#print(result)  # 5

# -- Returning terminates the function --


#def add(x, y):
#    return
#    print(x + y)
#    return x + y


#result = add(5, 8)  # Nothing printed out
#print(result)  # None, as is the first return

# -- Returning with conditionals --


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


result = divide(15, 3)
print(result)  # 5

another = divide(15, 0)
print(another)  # You fool!

#Coding exercise
student = {'name': 'Jose', 'school': 'Computing', 'grade': (66, 77, 88)}
#end

def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)
##end

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total = total + sum(student['grades']) #total += sum(student['grades'])
        count = count + len(student['grades']) #count += len(student['grades'])

    return total / count