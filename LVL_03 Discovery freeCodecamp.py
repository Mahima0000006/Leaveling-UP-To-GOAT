# ==========================================
# DEV LOG: LEVEL 03 - THE DISCOVERY
# ==========================================
# I found an amazing open-source platform called freeCodeCamp today.
# This file is a digital journal of my key learnings from the first modules.
#
# WHAT I LEARNED:
# 1. Python is a general-purpose language used everywhere (AI, Cyber, Web).
# 2. Variables are like labeled boxes. Professional coders use 'snake_case'.
# 3. Dynamic Typing: Python is smart and knows what data type is in the box.
# 4. type() is an X-Ray machine that tells you the exact data type.
# 5. isinstance() is the Security Guard that checks if data is correct.
# 6. BIGGEST LESSON: The input() function always captures data as a String!
# ==========================================

print(">>> INITIATING DEV LOG...\n")

# Using proper snake_case to define my variables
learning_platform = "freeCodeCamp"
modules_completed = 2
is_leveling_up = True

# Using the "Comma Trick" I learned to print easily with spaces
print("Today, I started training on", learning_platform)
print("I have successfully completed", modules_completed, "modules so far.\n")

# ------------------------------------------
# THE DATA X-RAY TEST
# ------------------------------------------
print(">>> RUNNING SYSTEM DIAGNOSTICS...")
print("The 'modules_completed' box contains:", type(modules_completed))
print("The 'is_leveling_up' box contains:", type(is_leveling_up), "\n")

# ------------------------------------------
# THE BUG FIX (SECURITY GUARD IN ACTION)
# ------------------------------------------
print(">>> LAUNCHING SECURITY GATEWAY...")

# Taking input from the user (Remember: This is always a String!)
security_code = input("Enter the secret 4-digit code to enter: ")

# Using .isdigit() to check if the string contains only numbers
if security_code.isdigit():
    print("Access Granted! Code format is secure.")
else:
    print("SECURITY ALERT: Invalid format! Code must be numbers only.")
