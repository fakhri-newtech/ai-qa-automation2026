import json

# =====================================================================
# --- MAGIC SETUP CODE (DO NOT CHANGE) ---
# This opens your data.json file and loads the arrays for you to use!
with open('data.json', 'r') as file:
    staging_data = json.load(file)

correct_password = staging_data["admin_credentials"]["correct_password"]
banned_users = staging_data["banned_users"]
request_users = staging_data["request_users"]
cart_totals = staging_data["cart_totals"]
legal_promo_codes = staging_data["legal_promo_codes"]
used_promo_codes = staging_data["used_promo_codes"]
# ---------------------------------------------------------------------

print("--- STARTING STAGING AUDIT SUITE ---")

# 1. AUTHENTICATION CHECK:
# Ask the user for a password. If it does not match 'correct_password', 
# print "Access Denied" and stop the script immediately. Otherwise, continue!


# 2. DYNAMIC THRESHOLD INPUT:
# Ask the user for a dynamic fraud limit threshold (and remember to cast it to a float!).


# 3. CREATE YOUR TRACKING LISTS:
# Create empty lists to store your test findings (e.g., security breaches, invalid carts, invalid promos, etc.).


# 4. WRITE YOUR TEST LOOPS & CONDITIONS:
# Plan and write your loops to audit:
# - Check if any banned users made requests (Security Audit)
# - Check cart totals against your rules (Financial Audit)
# - Check used promo codes against legal promo codes (Promo Validation)


# 5. PRINT YOUR FINAL QA TEST REPORT:
# print out a summary of your results!

print("--- AUDIT COMPLETE ---")