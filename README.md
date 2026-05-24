# Password Strength Analyzer

## Overview

Password Strength Analyzer is a Python-based cybersecurity project that evaluates the strength of user-entered passwords.

The application checks:
- Password length
- Password complexity
- Password uniqueness

It also suggests stronger passwords and stores passwords using an SQLite database to detect password reuse.

---

## Features

- Password strength checking
- Uppercase and lowercase validation
- Number and special character detection
- Password reuse detection
- Strong password generator
- SQLite database integration
- User feedback and suggestions

---

## Technologies Used

- Python
- SQLite
- Regular Expressions (`re`)
- Random Module
- String Module

---

## Project Structure

```text
password-strength-analyzer/
│
├── app.py
├── passwords.db
├── README.md
 
```

---

## How It Works

The program:
1. Takes a password from the user
2. Checks password strength
3. Gives suggestions to improve security
4. Stores the password in the SQLite database
5. Detects if the password was previously used
6. Generates a strong password suggestion

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/password-strength-analyzer.git
```

### Open Project Folder

```bash
cd password-strength-analyzer
```

### Run the Program

```bash
python app.py
```

---

## Example Output
 
=============================================
      PASSWORD STRENGTH ANALYZER
=============================================

Enter your password: Rahul@123

Password Strength: Strong

Password saved successfully.

Suggested Strong Password:
A#k9P@2mX!qL
```

---

## Database Used

This project uses SQLite database (`passwords.db`) for:
- Storing passwords
- Detecting password reuse

---

## Future Improvements

- Password hashing using SHA-256
- GUI using Tkinter
- Web version using Streamlit
- Password breach detection API
- Real-time password strength meter

---

## Learning Outcomes

This project helps in learning:
- Python programming
- Database integration
- Password security concepts
- Basic cybersecurity practices
- Regular expressions

 

 

## License

This project is developed for educational and internship purposes.
