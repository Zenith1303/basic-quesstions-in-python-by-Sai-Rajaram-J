character = input("Enter one English letter: ").strip()
letter = character.lower()
if len(character) != 1 or letter not in "abcdefghijklmnopqrstuvwxyz":
    print("Invalid input. Please enter one English letter.")
elif letter in "aeiou":
    print(character, "is a vowel.")
else:
    print(character, "is a consonant.")
