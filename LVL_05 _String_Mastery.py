# ==============================================================================
# DEV LOG: LEVEL 05 - STRING MASTERY (THEORY & PRACTICAL NOTES)
# ==============================================================================
# THEORY SUMMARY:
# 1. Strings are immutable: Once created, they cannot be modified.
# 2. Slicing: Uses [start:stop] where 'stop' is exclusive.
# 3. Concatenation: Uses '+' for joining. Use str() to convert non-strings.
# 4. Interpolation: F-strings (f'text {variable}') are the industry standard.
# 5. Methods: Tools like .upper(), .strip(), .find(), .split() act as shortcuts.
# ==============================================================================

print(">>> ACCESSING STRING MASTERY MODULE...\n")

# --- 1. STRING SLICING (The Ninja Tool) ---
# [start:stop:step]
# Remember: Start is inclusive, Stop is exclusive.
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]     # Extracts 'DEV'
last_three = employee_code[-3:]      # Extracts ID '001'
print(f"Department: {department}, ID: {last_three}\n")

# --- 2. FORMATTING & METHODS ---
raw_input = "  data analyst  "
clean_data = raw_input.strip().title() # Removes spaces and Capitalizes words
print(f"Cleaned: '{clean_data}'\n")

# --- 3. SEARCHING & DETECTIVES ---
# .find() returns index, .count() returns frequency
log = "ERROR: Failed login attempt"
print(f"Error found at index: {log.find('Failed')}")
print(f"Frequency of 'e': {log.count('e')}\n")

# --- 4. LIST TRANSFORMATION ---
# .split() converts string to list, .join() converts list to string
csv_data = "John,Doe,28"
data_list = csv_data.split(",") # ['John', 'Doe', '28']
new_csv = " - ".join(data_list)
print(f"New Format: {new_csv}")
