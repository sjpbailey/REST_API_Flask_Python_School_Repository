#f string

#name = "Boob"
#print(f"Hello, {name}")

#name = "Rolf"

#print(f"Hello, {name}")

#Template strings with .format()

#name = "Boob"
#greeting = "Hello, {}"
#with_name = greeting.format(name)
#with_name_two = greeting.format("Rolf")

#print(with_name)
#print(with_name_two)
# -- Using .format() --

# We can define template strings and then replace parts of it with another value, instead of doing it directly in the string.

greeting = "Hello, {}"
with_name = greeting.format("Rolf")
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)