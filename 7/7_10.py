dream_cation = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
   # Prompt for the person's name and country of dreamcation.
  name = input("\nWhat is your name? ")
  country = input("Which country would you like to visit for a dream vacation? ")

  # Store the country and name in the dictionary.
  dream_cation[name] = country

  # Find out if anyone else is going to take the poll.
  repeat = input("Would you like to let another person respond? (yes/ no) ")
  if repeat == 'no':
      polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, country in dream_cation.items():
    print(f"{name} would like to visit {country}.")
