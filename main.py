import random

print("🎮 Welcome to Number Guessing Game!")

print("\nChoose Difficulty")
print("1. Easy (1 - 50)")
print("2. Medium (1 - 100)")
print("3. Hard (1 - 500)")

choice = input("Enter your choice: ")

if choice == "1":
    secret_number = random.randint(1, 50)
    print("\nYou selected Easy Mode.")
    print("Guess a number between 1 and 50.")

elif choice == "2":
    secret_number = random.randint(1, 100)
    print("\nYou selected Medium Mode.")
    print("Guess a number between 1 and 100.")

elif choice == "3":
    secret_number = random.randint(1, 500)
    print("\nYou selected Hard Mode.")
    print("Guess a number between 1 and 500.")

else:
    print("Invalid choice! Defaulting to Medium Mode.")
    secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it correctly.")
        print(f"You guessed the number in {attempts} attempts.")
        break

    elif guess < secret_number:
        print("📉 Too Low!")

    else:
        print("📈 Too High!")