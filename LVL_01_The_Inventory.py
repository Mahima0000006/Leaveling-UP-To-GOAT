# LVL_02: The Inventory
# DEV NOTES:
# - I read the blueprint and figured out the logic completely on my own.
# - Mastered String Concatenation (gluing variables and words together with spaces).
# - Future goal: Start looking into how to secure these inputs so people can't inject bad code.

creature = input("What's your fav animal? ")
word = input("What word you use the most? ")
location = input("What place you visit Today? ")

print(creature + " sounds really like your fav animal and i heard you said " + word + " a lot " + location + " is a nice place")
