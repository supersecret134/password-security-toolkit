📌 Overview

This project is a cybersecurity learning toolkit designed to demonstrate password security concepts in a controlled and ethical environment.

It simulates real-world techniques used in password auditing, including:

Dictionary-based password testing
Brute-force simulation
Password strength analysis
Hash extraction (Linux /etc/shadow format demo)
Security audit reporting

⚠️ This project is strictly for educational and authorized lab use only.

🎯 Objectives
Understand password vulnerabilities
Simulate password cracking techniques
Analyze password strength and entropy
Demonstrate secure password practices
Generate security audit reports
🧠 Features
1. Smart Wordlist Generator
Target-based wordlist creation
Pattern-based mutations (suffixes, years, capitalization)
Optional use of rockyou.txt
2. Password Strength Analyzer
Complexity checking
Entropy estimation
Risk classification (Weak / Medium / Strong)
3. Dictionary Attack Module
Uses generated or external wordlists
Fast hash comparison using hashlib
4. Brute Force Simulator
Common password testing
Numeric brute-force (000000–999999)
Short character set brute-force (a-z, 0-9)
5. Hash Extraction Module
Simulates Linux /etc/shadow parsing
Identifies system users and hash formats
6. Security Report Generator
Logs all test results
Risk classification
Security score calculation
Recommendations for improvement
🛠️ Tech Stack
Python 3
hashlib
os module
itertools
time module
📁 Project Structure
password-security-toolkit/
│
├── main.py
├── modules/
│   ├── dictionary.py
│   ├── brute_force.py
│   ├── strength.py
│   ├── cracker.py
│   ├── hash_extractor.py
│   ├── hash_utils.py
│   ├── report.py
│
├── data/
│   └── wordlist.txt (generated)
│
├── results/
│   └── report.txt
│
└── README.md
⚙️ How to Run
python3 main.py
📊 Example Output
Password strength rating
Cracked password (if found in wordlist)
Brute-force attempts
Security audit report
⚠️ Ethical Notice

This tool is built for:

Cybersecurity education
Penetration testing labs
Academic projects

🚫 Do NOT use it against systems you do not own or have permission to test.

🚀 Future Improvements
AI-based password prediction
GPU-accelerated cracking simulation
Web dashboard UI
Advanced entropy scoring model
👨‍💻 Author

Cybersecurity Toolkit Project (Educational Simulation)

⭐ License

For educational use only.
