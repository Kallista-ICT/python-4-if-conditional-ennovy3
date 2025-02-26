# Ask for the user's birth year
birth_year = int(input("Please enter your input your birth year (e.g., 2000): "))

# Determine category/level based on user input
if birth_year < 1946:                        # First threshold condition
   generation = "Silent Generation"      # Category for the first condition
elif birth_year < 1965:                      # Second threshold condition
   generation = "Baby boomer"            # Category for the second condition
elif birth_year < 1981:                      # Third threshold condition
   generation = "Generation X"           # Category for the third condition 
elif birth_year < 1997:                      # Fourth threshold category
   generation = "Millenials"             # Category for the fourth condition
elif birth_year < 2013:                      # Fifth threshold category
   generation = "Generation Z"           # Category for the fifth condition
else:                                   # Default condition for all the other cases
   generation = "Generation Alpha"       # Default category for all the else condition
print(f"You belong to: {generation}")