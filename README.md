📌 Overview

This project is a cybersecurity learning toolkit designed to demonstrate password security concepts in a controlled and ethical environment.

It simulates real-world techniques used in password auditing, including:

Dictionary-based password testing
Brute-force simulation
Password strength analysis
Simulated hash extraction based on Linux /etc/shadow format
Security audit reporting

⚠️ This project is strictly for educational and authorized lab use only.

🎯 Objectives
Understand password vulnerabilities
Simulate password cracking techniques
Analyze password strength and entropy
Demonstrate secure password practices
Generate security audit reports
🧠 Features
🔹 Smart Wordlist Generator
Target-based wordlist creation
Pattern-based mutations (suffixes, years, capitalization)
Optional use of rockyou.txt
🔹 Password Strength Analyzer
Complexity checking
Entropy estimation
Risk classification (Weak / Medium / Strong)
🔹 Dictionary Attack Module
Uses generated or external wordlists
Fast hash comparison using hashlib
🔹 Brute Force Simulator
Common password testing
Numeric brute-force (000000–999999)
Short charset brute-force (a–z, 0–9)
🔹 Hash Extraction Module
Simulates Linux /etc/shadow parsing
Identifies users and hash formats
🔹 Security Report Generator
Logs all test results
Risk classification
Security score calculation
Recommendations for improvement
🔄 Workflow
User selects a module from CLI
Wordlist is generated or loaded
Hash is extracted (simulated)
Dictionary / brute-force attack is executed
Password strength is analyzed
Results are stored
Final security audit report is generated
📊 Flowchart (Text Version)
START
↓
Input Data
↓
Generate Wordlist
↓
Extract Hash (Demo)
↓
Run Dictionary / Brute Force Attack
↓
Analyze Password Strength
↓
Generate Report
↓
END
🛠️ Tech Stack
Python 3
hashlib
os
itertools
time
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
│   └── wordlist.txt
│
├── results/
│   └── report.txt
│
└── README.md
⚙️ How to Run (Local)
python3 main.py
☁️ Run on GitHub Codespaces

You can run this project directly in the browser without installing anything.

Steps:
Open the repository on GitHub
Click Code
Go to the Codespaces tab
Click Create Codespace on main
Wait for the environment to load
Run:
python main.py
Expected Output:
=== Advanced Credential Toolkit ===
1. Generate Wordlist
2. Check Password Strength
3. Dictionary Attack
4. Brute Force Attack
5. Hash Extraction (Linux/Windows)
6. Generate Report
7. Exit
📈 Expected Output
Generated wordlist file
Password strength classification
Cracked passwords (if vulnerable)
Number of attempts and time taken
Security audit report with recommendations
📊 Example Output
Password strength rating
Cracked password (if found)
Brute-force attempt logs
Final security report
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
