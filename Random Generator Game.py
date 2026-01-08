import random

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def check_guess(random_num, user_guess):
    return random_num == user_guess

print("Welcome to the Guess the Number Game!")
print("I have selected a random number between 1 and 100. Try to guess it!")

secret = generate_random_number(1, 100)
attempts = 0
extra_hint_given = False

while True:
    try:
        user_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if check_guess(secret, user_guess):
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break
    else:
        if user_guess < secret:
            print("Incorrect! Try a higher number.")
        else:
            print("Incorrect! Try a lower number.")


        if attempts >= 3 and not extra_hint_given:
            extra_hint_given = True
            hint_type = random.choice(["even_odd", "multiple_of_5", "power_check"])
            if hint_type == "even_odd":
                if secret % 2 == 0:
                    print("Hint: The number is even.")
                else:
                    print("Hint: The number is odd.")
            elif hint_type == "multiple_of_5":
                if secret % 5 == 0:
                    print("Hint: The number is a multiple of 5.")
                else:
                    print("Hint: The number is NOT a multiple of 5.")
            else:
                if secret ** 2 > 1000:
                    print("Hint: The square of the number is greater than 1000.")
                else:
                    print("Hint: The square of the number is less than or equal to 1000.")
