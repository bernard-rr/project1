# a = 33
# b = 100
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b") 

# score = 53
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# age = 2.5
# if age < 5:
#     print("Free")
# elif age >= 5 and age <= 12:
#     print("$10 child ticket")
# elif age >= 65:
#     print("$12 senior ticket")
# else:
#     print("$20 regular ticket")

# username = "use123"
# password = "secret123"
# if username == "admin" and password == "admin123":
#     print("Admin access granted")
# elif username == "user123" and password == "secret123":
#     print("User access granted")
# else:
#     print("Access denied")

# import datetime
# hour = datetime.datetime.now().hour
# if hour < 12:
#     print("Good morning!")
# elif hour < 17:
#     print("Good afternoon!")
# else:
#     print("Good evening!")
##########################################
# print("Welcome to the Ice Cream Parlor!")
# flavor = input("Choose your ice cream flavor (chocolate, vanilla, strawberry): ")
# if flavor == "chocolate":
#     print("You picked chocolate! Enjoy your delicious treat.")
# elif flavor == "vanilla":
#     print("Vanilla is a classic choice! Enjoy your ice cream.")
# elif flavor == "strawberry":
#     print("Strawberry is a fruity delight! Enjoy your ice cream.")
# else:
#     print("Sorry, we don't have that flavor. Please choose from the options.")
###################
# print("Welcome to the Adventure Game!")
# choice = input("You find a treasure chest. Do you want to 'open' it or 'leave' it? ")
# if choice == "open":
#     print("You found a treasure! You win the game!")
# elif choice == "leave":
#     print("You decided to leave the chest. The adventure continues.")
# else:
#     print("Invalid choice. Please decide to 'open' or 'leave' the treasure chest.")
# ####################
# print("Let's play the Animal Guessing Game!")
# animal = input("I'm thinking of an animal. Is it a 'dog' or a 'cat'? ")
# if animal == "dog":
#     print("Woof! You guessed it right, it's a dog!")
# elif animal == "cat":
#     print("Meow! You guessed it right, it's a cat!")
# else:
#     print("Sorry, that's not one of the options. Try again with 'dog' or 'cat'.")

##########################
# print("Let's make a pizza!")
# topping = input("Choose a pizza topping (pepperoni, mushrooms, or peppers): ")
# if topping == "pepperoni":
#     print("Pepperoni is a classic choice for pizza!")
# elif topping == "mushrooms":
#     print("Mushrooms add a unique flavor to your pizza!")
# elif topping == "peppers":
#     print("Peppers give your pizza a spicy kick!")
# else:
#     print("Sorry, we don't have that topping. Please choose from the options.")


##################################
print("You are in a magical land with three doors!")
door = input("Which door will you choose (1, 2, 3)? ")
if door == "1":
    print("You found a hidden treasure! Congratulations!")
elif door == "2":
    print("A friendly dragon appears and offers you a wish. What do you wish for?")
    wish = input("I wish for: ")
    print(f"You wished for {wish}. The dragon grants your wish!")
elif door == "3":
    print("Oops! You fell into a pit, but a helpful squirrel rescues you.")
else:
    print("Invalid choice. Please choose a door (1, 2, or 3).")



