def welcome_user():
  """
  Asks the user for their name and prints a personalized welcome message, Tron Legacy style.
  """
  user_name = input("Identify yourself, Program: ") # Ask for the user's name

  # --- NEW LOGIC: Using an if/else statement to check the name ---
  if user_name == "Gary": # Check if the name entered is exactly "Gary"
    # If the name IS "Gary", print this special greeting:
    print(f"Greetings Creator! Welcome, {user_name}.")
  else:
    # If the name IS NOT "Gary", print the regular greeting:
    print(f"Greetings, Program! Welcome, {user_name}.")
  # --- End of new logic ---

# Example usage:
# This will now prompt the user for their name,
# and then apply the special or regular greeting based on the input.
welcome_user()