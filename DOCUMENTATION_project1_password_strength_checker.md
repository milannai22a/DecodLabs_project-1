# 📘 Documentation — Password Strength Checker

> **Author:** [milannai22a](https://github.com/milannai22a)
> **Repository:** [DecodLabs_project-1](https://github.com/milannai22a/DecodLabs_project-1)
> **Type:** Command-Line Application
> **Language:** Python 3.x (built-in libraries only)
> **Submission:** DecodLabs — Project 1

---

## 📋 Table of Contents

1. [Project Overview](#1-project-overview)
2. [Objectives](#2-objectives)
3. [Technology Used](#3-technology-used)
4. [Project Structure](#4-project-structure)
5. [How to Run](#5-how-to-run)
6. [Program Flow](#6-program-flow)
7. [Strength Evaluation Logic](#7-strength-evaluation-logic)
8. [Built-in Libraries Used](#8-built-in-libraries-used)
9. [Sample Terminal Output](#9-sample-terminal-output)
10. [Test Cases](#10-test-cases)
11. [Known Limitations](#11-known-limitations)
12. [Future Improvements](#12-future-improvements)

---

## 1. Project Overview

The **Password Strength Checker** is a terminal-based Python application that analyses a user-entered password and rates its strength. The program runs entirely from the command line — the user is prompted to enter a password, and the tool instantly outputs a strength rating (Weak, Moderate, or Strong) along with a score and feedback on how to improve it.

This project uses **only Python's built-in standard library** — no third-party packages are required.

---

## 2. Objectives

- Accept a password as input from the user via the terminal
- Evaluate the password against a set of security rules
- Return a clear strength rating and improvement suggestions
- Demonstrate Python string manipulation, conditionals, and loops
- Use only built-in Python — no pip installs required

---

## 3. Technology Used

| Item | Detail |
|---|---|
| Language | Python 3.x |
| Interface | Terminal / Command Line |
| Libraries | Built-in only (`string`, `re`, or manual checks) |
| Dependencies | None — no `pip install` needed |
| Platform | Windows, macOS, Linux |

---

## 4. Project Structure

```
DecodLabs_project-1/
│
├── password_checker.py     # Main script — all logic lives here
└── README.md               # Project readme
```

All the logic — input handling, rule checking, scoring, and output — is contained in the single file `password_checker.py`.

---

## 5. How to Run

### Step 1 — Make sure Python is installed
```bash
python --version
# Should show Python 3.x
```

### Step 2 — Clone the repository
```bash
git clone https://github.com/milannai22a/DecodLabs_project-1.git
cd DecodLabs_project-1
```

### Step 3 — Run the script
```bash
python password_checker.py
```

### Step 4 — Enter your password when prompted
```
Enter your password: ___
```

No virtual environment or package installation needed.

---

## 6. Program Flow

```
START
  │
  ▼
Prompt user: "Enter your password:"
  │
  ▼
Read password input from terminal
  │
  ▼
Run 5 rule checks on the password:
  ├── Check length (>= 8 chars?)
  ├── Check for uppercase letters
  ├── Check for lowercase letters
  ├── Check for digits
  └── Check for special characters
  │
  ▼
Calculate total score (0–5)
  │
  ▼
Determine strength rating:
  ├── Score 0–2 → Weak
  ├── Score 3–4 → Moderate
  └── Score 5   → Strong
  │
  ▼
Print strength, score, and feedback to terminal
  │
  ▼
END
```

---

## 7. Strength Evaluation Logic

The password is evaluated against **5 rules**. Each rule that passes adds 1 point to the score.

### Rules

| # | Rule | How It's Checked |
|---|---|---|
| 1 | Length ≥ 8 characters | `len(password) >= 8` |
| 2 | Contains uppercase letter | `any(c.isupper() for c in password)` |
| 3 | Contains lowercase letter | `any(c.islower() for c in password)` |
| 4 | Contains a digit | `any(c.isdigit() for c in password)` |
| 5 | Contains a special character | `any(c in "!@#$%^&*..." for c in password)` |

### Scoring Table

| Score | Rating |
|---|---|
| 0 – 2 | ❌ Weak |
| 3 – 4 | ⚠️ Moderate |
| 5 | ✅ Strong |

### Python Logic

```python
def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Rule 2: Uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Rule 3: Lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Rule 4: Digit
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Rule 5: Special character
    special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    if any(c in special_chars for c in password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$ etc.).")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, feedback


# Main program
password = input("Enter your password: ")
strength, score, feedback = check_password_strength(password)

print(f"\nStrength : {strength}")
print(f"Score    : {score} / 5")

if feedback:
    print("Feedback :")
    for tip in feedback:
        print(f"  - {tip}")
else:
    print("Feedback : Great! Your password meets all the criteria.")
```

---

## 8. Built-in Libraries Used

This project uses **no external libraries**. All functionality is achieved with Python's built-in tools:

| Feature | How It's Done |
|---|---|
| User input | `input()` |
| String checks | `.isupper()`, `.islower()`, `.isdigit()` |
| Iteration | `any()` with a generator expression |
| Length check | `len()` |
| Output | `print()`, f-strings |

---

## 9. Sample Terminal Output

**Strong password:**
```
Enter your password: MyP@ssw0rd!

Strength : Strong
Score    : 5 / 5
Feedback : Great! Your password meets all the criteria.
```

**Moderate password:**
```
Enter your password: Hello1234

Strength : Moderate
Score    : 4 / 5
Feedback :
  - Add at least one special character (!@#$ etc.).
```

**Weak password:**
```
Enter your password: hello

Strength : Weak
Score    : 2 / 5
Feedback :
  - Use at least 8 characters.
  - Add at least one uppercase letter (A-Z).
  - Add at least one number (0-9).
  - Add at least one special character (!@#$ etc.).
```

---

## 10. Test Cases

| Password | Expected Score | Expected Rating |
|---|---|---|
| `abc` | 2 | Weak |
| `abcdefgh` | 3 | Moderate |
| `Abcdefgh` | 4 | Moderate |
| `Abcdefg1` | 4 | Moderate |
| `Abcdef1!` | 5 | Strong |
| `P@ssw0rd` | 5 | Strong |
| `12345678` | 2 | Weak |
| `PASSWORD` | 3 | Moderate |

---

## 11. Known Limitations

- Does not check against a list of commonly used passwords (e.g. `password123`)
- Does not detect repeated characters or keyboard patterns (e.g. `aaaa`, `qwerty`)
- Password is visible while typing (no hidden input — `getpass` not used)
- Single-run program — exits after one check

---

## 12. Future Improvements

- Hide password input using Python's built-in `getpass` module
- Check against a dictionary of the top 1000 weak passwords
- Detect repeated characters and common patterns
- Allow the user to check multiple passwords in a loop without restarting
- Add color-coded output using `colorama` (optional third-party)
- Export results to a text file

---

*Documentation last updated: May 2026*
