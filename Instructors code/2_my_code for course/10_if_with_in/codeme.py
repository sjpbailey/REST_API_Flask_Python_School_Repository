# -- modified lower case and abs absolute 

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input in ("y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")
