# LVL_02: The Alchemist 
# DEV NOTES:
# - I learned the critical difference between Strings (text) and Integers (numbers).
# - I mastered "Type Casting" using int() to do math, and str() to print results.
# - I built THREE separate security calculation tools in one script.

print(">>> INITIATING SECURITY TOOLKIT...\n")

# --- TOOL 1: THE PAYLOAD CALCULATOR (+) ---
print("--- TOOL 1: THE PAYLOAD CALCULATOR ---")
patch_a = int(input("What is the size of Patch A (in MB)? "))
patch_b = int(input("What is the size of Patch B (in MB)? "))
total_payload = patch_a + patch_b
print("Total payload is " + str(total_payload) + " MB. Ready to deploy!\n")

# --- TOOL 2: THE FIREWALL BREACH (-, *) ---
print("--- TOOL 2: THE FIREWALL BREACH ---")
hp = int(input("What is the firewall's starting HP? "))
dps = int(input("How much damage is the rogue AI doing per second? "))
total_hit = dps * 10
remaining_hp = hp - total_hit
print("After 10 seconds, Firewall HP will be at: " + str(remaining_hp) + "\n")

# --- TOOL 3: THE BUG BOUNTY SPLITTER (/) ---
print("--- TOOL 3: THE BUG BOUNTY SPLITTER ---")
payout = int(input("What was the total Bug Bounty payout? "))
users = int(input("How many hackers were in your team? "))
new_money = payout / users
print("Initiating wire transfer. Each hacker receives $" + str(new_money))
