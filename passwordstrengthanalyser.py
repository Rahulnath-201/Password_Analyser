import re
import sqlite3
import random
import string

# ===================================
# DATABASE CONNECTION
# ===================================

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password TEXT
)
""")

conn.commit()

# ===================================
# CHECK PASSWORD STRENGTH
# ===================================

def check_password_strength(password):

    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Number Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special Character Check
    if re.search(r"[!@#$%^&*()]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Password Reuse Check
    cursor.execute(
        "SELECT * FROM passwords WHERE password = ?",
        (password,)
    )

    reused = cursor.fetchone()

    if reused:
        feedback.append("Password already used before.")

    # Strength Level
    if score <= 2:
        strength = "Weak"

    elif score == 3 or score == 4:
        strength = "Medium"

    else:
        strength = "Strong"

    return strength, feedback

# ===================================
# GENERATE STRONG PASSWORD
# ===================================

def generate_password():

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    password = ""

    for i in range(12):
        password += random.choice(characters)

    return password

# ===================================
# MAIN PROGRAM
# ===================================

print("=" * 45)
print("      PASSWORD STRENGTH ANALYZER")
print("=" * 45)

password = input("\nEnter your password: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

# Display Suggestions
if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)

# Store Password in Database
cursor.execute(
    "INSERT INTO passwords(password) VALUES(?)",
    (password,)
)

conn.commit()

print("\nPassword saved successfully.")

# Suggested Password
print("\nSuggested Strong Password:")
print(generate_password())

# Close Database
conn.close()