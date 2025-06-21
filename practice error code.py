# This script greets the user and calculates a “lucky number”

user_name = input("Hello! What’s your name? ")

# --- NEW: Ask the user for their favorite number! ---
# We use int() to convert the text input into a whole number for calculations.
try:
    favorite_number = int(input("What's your favorite number? "))
except ValueError:
    print("That's not a valid number! I'll use 7 for you.")
    favorite_number = 7 # Default if they don't enter a number
# --- END NEW ---

print(f"Nice to meet you, {user_name}!")

# Now calculate a lucky number based on THEIR favorite number!
lucky_number = favorite_number * 2

print(f"Your lucky number is: {lucky_number}")

print("Have a great day!")
