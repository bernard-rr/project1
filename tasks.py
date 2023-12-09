# favorite_fruits = ["pineapple", "banana", "mango", "apple", "orange"]

# fruit_num = 1
# for fruit in favorite_fruits:
#     print("Favorite Fruit", fruit_num, fruit)
#     fruit_num += 1

# first_fruit = favorite_fruits[0]
# print(first_fruit)

# second_fruit = favorite_fruits[1]
# print(second_fruit)

# third_fruit = favorite_fruits[2]
# print(third_fruit)

import random
random_number = random.randint(1, 20)

guess = 0
while guess != random_number:
    guess = int(input("Guess the number (between 1 and 20): "))
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break