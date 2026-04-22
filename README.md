# 🔐 Password Cracking & Credential Attack Suite

## 📌 Overview
This project is a cybersecurity learning toolkit designed to demonstrate password security concepts in a controlled and ethical environment.

It simulates real-world techniques used in password auditing, including:
- Dictionary-based password testing  
- Brute-force simulation  
- Password strength analysis  
- Simulated hash extraction (Linux /etc/shadow format)  
- Security audit reporting  

⚠️ This project is strictly for educational and authorized lab use only.

---

## 🎯 Objectives
- Understand password vulnerabilities  
- Simulate password cracking techniques  
- Analyze password strength and entropy  
- Demonstrate secure password practices  
- Generate security audit reports  

---

## 🧠 Features

### Smart Wordlist Generator
- Target-based wordlist creation  
- Pattern-based mutations (suffixes, years, capitalization)  
- Optional use of rockyou.txt  

### Password Strength Analyzer
- Complexity checking  
- Entropy estimation  
- Risk classification (Weak / Medium / Strong)  

### Dictionary Attack Module
- Uses generated or external wordlists  
- Fast hash comparison using hashlib  

### Brute Force Simulator
- Common password testing  
- Numeric brute-force (000000–999999)  
- Short charset brute-force (a–z, 0–9)  

### Hash Extraction Module
- Simulates Linux /etc/shadow parsing  
- Identifies users and hash formats  

### Security Report Generator
- Logs all test results  
- Risk classification  
- Security score calculation  
- Recommendations for improvement  

---

## 🔄 Workflow
1. User selects a module from CLI  
2. Wordlist is generated or loaded  
3. Hash is extracted (simulated)  
4. Dictionary / brute-force attack is executed  
5. Password strength is analyzed  
6. Results are stored  
7. Final security audit report is generated  

---

## 🛠️ Tech Stack
- Python 3  
- hashlib  
- os  
- itertools  
- time  

---

## ⚙️ How to Run
python3 main.py

---

## ☁️ Run on GitHub Codespaces
1. Open repository on GitHub  
2. Click Code  
3. Go to Codespaces tab  
4. Click "Create Codespace on main"  
5. Run: python main.py  

---

## 📈 Expected Output
- Generated wordlist  
- Password strength results  
- Cracked passwords (if weak)  
- Attempt logs  
- Security audit report  

---

## ⚠️ Ethical Notice
This tool is for:
- Cybersecurity education  
- Penetration testing labs  
- Academic projects  

🚫 Do NOT use it on unauthorized systems.

---

## 🚀 Future Improvements
- AI-based password prediction  
- GPU-based cracking simulation  
- Web dashboard UI  
- Advanced entropy analysis  

---

## 👨‍💻 Author
Cybersecurity Toolkit Project (Educational Use)

---

## ⭐ License
For educational use only.
