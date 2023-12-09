# Define a function called greet()
def greet():
    print("Hello, everyone!")

# Calling the function
greet()  # This will print "Hello, everyone!"

# Define a function called greet_person() with an argument
def greet_person(name):
    print("Hello,", name)

# Calling the function with an argument
greet_person("Chidi-Bernard") 

# Define a function called square() that returns a value
def square(number):
    return number * number



# A long function to calculate statistics for a list of numbers
def calculate_statistics(numbers):
    # Step 1: Calculate the total number of elements in the list
    count = len(numbers)

    # Step 2: Calculate the sum of all elements in the list
    total = sum(numbers)

    # Step 3: Calculate the mean (average) of the numbers
    mean = total / count if count > 0 else 0

    # Step 4: Sort the list in ascending order
    sorted_numbers = sorted(numbers)

    # Step 5: Check if the count of numbers is even or odd
    if count % 2 == 0:  # If count is even
        # Calculate the median for even count
        median = (sorted_numbers[count // 2 - 1] + sorted_numbers[count // 2]) / 2
    else:  # If count is odd
        # Calculate the median for odd count
        median = sorted_numbers[count // 2]

    # Step 6: Find the minimum and maximum values in the list
    minimum = min(numbers) if count > 0 else 0
    maximum = max(numbers) if count > 0 else 0

    # Step 7: Print or return the calculated statistics
    print("Total count:", count)
    print("Sum:", total)
    print("Mean (Average):", mean)
    print("Median:", median)
    print("Minimum:", minimum)
    print("Maximum:", maximum)

# Example usage of the calculate_statistics function
numbers_list = [7, 12, 5, 21, 8, 10, 15]
calculate_statistics(numbers_list)


import random

# Function for a guessing game
def guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Guessing Game! I'm thinking of a number between 1 and 20.")

    for attempts_taken in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempts_taken}/{max_attempts}: Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the correct number ({secret_number}) in {attempts_taken} attempts!")
            break

        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")

# Calling the guessing_game function
guessing_game()



