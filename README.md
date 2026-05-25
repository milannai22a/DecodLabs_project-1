[README_project1_password_strength_checker.md](https://github.com/user-attachments/files/28209852/README_project1_password_strength_checker.md)
# 🔐 Password Strength Checker

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Terminal](https://img.shields.io/badge/Runs_In-Terminal-black?style=for-the-badge&logo=gnometerminal)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen?style=for-the-badge)
![DecodLabs](https://img.shields.io/badge/DecodLabs-Project_1-orange?style=for-the-badge)

A terminal-based **Password Strength Checker** built entirely with Python's built-in libraries. No pip installs required — just run and go.

---

## 📌 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [License](#license)

---

## 📖 About

This is a **command-line tool** that evaluates the strength of a password entered by the user directly in the terminal. It checks the password against a set of security rules and gives a score along with feedback. Built as a DecodLabs submission using only Python's standard library.

---

## ✨ Features

- ✅ Runs entirely in the terminal — no browser needed
- ✅ Zero external dependencies — only built-in Python
- ✅ Checks length, uppercase, lowercase, digits, and special characters
- ✅ Returns a strength rating: **Weak**, **Moderate**, or **Strong**
- ✅ Provides specific feedback on what to improve

---

## ⚙️ Requirements

- Python 3.x (no additional packages needed)

Check your Python version:
```bash
python --version
```

---

## ▶️ How to Run

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/milannai22a/DecodLabs_project-1.git
   cd DecodLabs_project-1
   ```

2. **Run the script:**
   ```bash
   python password_checker.py
   ```

3. **Enter your password** when prompted in the terminal.

---

## ⚙️ How It Works

The script checks your password against 5 rules, each worth 1 point:

| Rule | Condition |
|---|---|
| Length | At least 8 characters |
| Uppercase | At least one A–Z letter |
| Lowercase | At least one a–z letter |
| Digit | At least one number (0–9) |
| Special Character | At least one symbol like `!@#$%^&*` |

**Scoring:**

| Score | Strength |
|---|---|
| 0 – 2 | ❌ Weak |
| 3 – 4 | ⚠️ Moderate |
| 5 | ✅ Strong |

---

## 🖥️ Sample Output

```
Enter your password: MyP@ss99

Strength : Strong
Score    : 5 / 5
Feedback : Great! Your password meets all the criteria.
```

```
Enter your password: hello

Strength : Weak
Score    : 2 / 5
Feedback :
  - Use at least 8 characters.
  - Add at least one uppercase letter.
  - Add at least one number.
  - Add at least one special character.
```

---

## 📁 Project Structure

```
DecodLabs_project-1/
│
├── password_checker.py     # Main Python script
└── README.md               # Project documentation
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Made with ❤️ by [milannai22a](https://github.com/milannai22a) | DecodLabs Submission
