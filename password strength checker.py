# =======================================================================================================================
# password strength checker
# description: analyses password strength based on length, uppercase letters, numbers and special symbols.
# =======================================================================================================================

import string

# common password list
COMMON_PASSWORDS = [
    "password", "admin", "admin123", "hello", "hello123",
    "cricket123", "root", "pass", "12345678", "abc123"
]


# check password length and return score + feedback
def check_length(password):
    length = len(password)
    if length < 6:
        return 0, f"too short ({length} characters). minimum 8 recommended."
    elif length < 8:
        return 1, f"length is acceptable ({length} characters)."
    else:
        return 2, f"length is good ({length} characters)."


# check for uppercase letters
def check_uppercase(password):
    count = sum(1 for c in password if c.isupper())
    if count == 0:
        return 0, "no uppercase letters. add at least one (A-Z)."
    elif count == 1:
        return 1, "1 uppercase letter. add more for better strength."
    else:
        return 2, f"{count} uppercase letters found. excellent."


# check for numbers
def check_numbers(password):
    count = sum(1 for c in password if c.isdigit())
    if count == 0:
        return 0, "no numbers found. add more digits."
    elif count == 1:
        return 1, "1 number found. add more digits."
    else:
        return 2, f"{count} numbers found. good."


# check for symbols
def check_symbols(password):
    special_chars = string.punctuation
    count = sum(1 for c in password if c in special_chars)
    if count == 0:
        return 0, "no special characters found. add symbols like !@#$."
    elif count == 1:
        return 1, "1 special character found. add more for better strength."
    else:
        return 2, f"{count} special characters found. good."


# check for common passwords
def check_common(password):
    if password.lower() in COMMON_PASSWORDS:
        return True, "this is a very common password. change it immediately."
    return False, "not a common password. good."


# check for repeated characters (e.g. "aaa", "111")
def check_repeated_chars(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True, "repeated characters found (e.g. 'aaa'). avoid patterns."
    return False, "no repeated character patterns found."


# show the password strength based on score
def classify_strength(score, max_score):
    percentage = (score / max_score) * 100
    if percentage < 40:
        return "Weak", percentage
    elif percentage < 70:
        return "Medium", percentage
    else:
        return "Strong", percentage


# analyse the password and return the report
def analyse_password(password):
    print("\n" + "=" * 55)
    print("       password strength checker ")
    print("=" * 55)
    print(f"   analysing: {'*' * len(password)}")
    print("-" * 55)

    total_score = 0
    max_score = 8  # 2+2+2+2 from length/upper/nums/symbols

    # step 1 - check for common passwords
    is_common, common_msg = check_common(password)
    print(f"\n   [1] common password check")
    print(f"       {common_msg}")
    if is_common:
        print(f"\n   result: WEAK — common password detected. change your password immediately.")
        print("=" * 55)
        return "Weak"

    # step 2 - check length
    length_score, length_msg = check_length(password)
    total_score += length_score
    print(f"\n   [2] length check             score: {length_score}/2")
    print(f"       {length_msg}")

    # step 3 - check uppercase
    uppercase_score, uppercase_msg = check_uppercase(password)
    total_score += uppercase_score
    print(f"\n   [3] uppercase letters        score: {uppercase_score}/2")
    print(f"       {uppercase_msg}")

    # step 4 - check numbers
    num_score, num_msg = check_numbers(password)
    total_score += num_score
    print(f"\n   [4] numbers                  score: {num_score}/2")
    print(f"       {num_msg}")

    # step 5 - check symbols
    sym_score, sym_msg = check_symbols(password)
    total_score += sym_score
    print(f"\n   [5] special symbols          score: {sym_score}/2")
    print(f"       {sym_msg}")

    # step 6 - check repeated characters (penalty)
    has_repeat, repeat_msg = check_repeated_chars(password)
    print(f"\n   [6] repeated chars check")
    print(f"       {repeat_msg}")
    if has_repeat:
        total_score -= 2

    # final score and classification
    total_score = max(0, total_score)
    strength, percentage = classify_strength(total_score, max_score)

    print(f"\n   total score: {total_score}/{max_score}  ({percentage:.1f}%)")
    print(f"   strength   : {strength}")

    # recommendations
    print("\n   recommendations:")
    if length_score < 2:
        print("   -> use at least 12 characters for a strong password.")
    if uppercase_score < 2:
        print("   -> add more uppercase characters (A-Z).")
    if num_score < 2:
        print("   -> add more numbers (0-9).")
    if sym_score < 2:
        print("   -> add more symbols (e.g. !@#$%^&*).")
    if has_repeat:
        print("   -> avoid repeated characters like 'aaa' or '111'.")
    if strength == "Strong":
        print("   -> great password! keep it safe.")

    print("=" * 55 + "\n")
    return strength


def main():
    print("\n" + "=" * 55)
    print("       decodlabs project-1")
    print("       password strength checker")
    print("=" * 55)

    while True:
        print("\n options:")
        print("   1. check a password.")
        print("   2. exit")
        choice = input("\n   enter choice (1/2): ").strip()

        if choice == "1":
            password = input("\n   enter password to check: ").strip()
            if not password:
                print("   error: password cannot be empty.")
                continue
            analyse_password(password)

        elif choice == "2":
            print("\n   exiting password checker. stay safe.")
            print("   developed by milan nai")
            break

        else:
            print("   invalid choice. enter 1 or 2.")


if __name__ == "__main__":
    main()