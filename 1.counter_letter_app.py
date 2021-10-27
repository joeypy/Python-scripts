print("Welcome to the Letter Counter App")

name = input("\nWhat is your name: ").title().strip()

print(f"Hello {name}!")
print("\nI will count the number of times that a specific letter occurs in a message.")

text = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occurrences of: ")
counter = text.count(letter)
print(f"\n{name}, your message has {counter} {letter}'s in it.")
