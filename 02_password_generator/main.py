import random
import string
import pyperclip

print("=" * 45)
print("        🔐 PROFESSIONAL PASSWORD GENERATOR")
print("=" * 45)

while True:
    try:
        length = int(input("\nEnter password length: "))

        if length < 4:
            print("❌ Password length must be at least 4.")
            continue

    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    uppercase = input("Include Uppercase Letters? (y/n): ").lower()
    lowercase = input("Include Lowercase Letters? (y/n): ").lower()
    numbers = input("Include Numbers? (y/n): ").lower()
    symbols = input("Include Symbols? (y/n): ").lower()

    password = []
    characters = ""

    if uppercase == "y":
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if lowercase == "y":
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if numbers == "y":
        characters += string.digits
        password.append(random.choice(string.digits))

    if symbols == "y":
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if characters == "":
        print("❌ Please select at least one character type.")
        continue

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print("\n" + "=" * 45)
    print("✅ Generated Password:")
    print(password)
    print("=" * 45)

    # Password Strength
    if length < 8:
        print("Strength: 🔴 Weak")
    elif length < 12:
        print("Strength: 🟡 Medium")
    else:
        print("Strength: 🟢 Strong")

    # Copy to Clipboard
    pyperclip.copy(password)
    print("📋 Password copied to clipboard!")

    # Save Password
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

    print("💾 Password saved to passwords.txt")

    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("\n👋 Thank you for using Password Generator!")
        break