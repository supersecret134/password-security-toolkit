# 🔐 Password Cracking & Credential Attack Suite

## 📌 OVERVIEW
This project is a cybersecurity learning toolkit designed to demonstrate password security concepts in a controlled and ethical environment.

It simulates real-world techniques used in password auditing, including:

- Dictionary-based password testing  
- Brute-force simulation  
- Password strength analysis  
- Simulated hash extraction (Linux /etc/shadow format)  
- Security audit reporting  

⚠️ This project is strictly for educational and authorized lab use only.

---

## 🎯 OBJECTIVES
- Understand password vulnerabilities  
- Simulate password cracking techniques  
- Analyze password strength and entropy  
- Demonstrate secure password practices  
- Generate security audit reports  

---

## 🧠 FEATURES

### 1. Smart Wordlist Generator
- Target-based wordlist creation  
- Pattern-based mutations (suffixes, years, capitalization)  
- Optional use of rockyou.txt  

### 2. Password Strength Analyzer
- Complexity checking  
- Entropy estimation  
- Risk classification (Weak / Medium / Strong)  

### 3. Dictionary Attack Module
- Uses generated or external wordlists  
- Fast hash comparison using hashlib  

### 4. Brute Force Simulator
- Common password testing  
- Numeric brute-force (000000–999999)  
- Short charset brute-force (a–z, 0–9)  

### 5. Hash Extraction Module
- Simulates Linux /etc/shadow parsing  
- Identifies users and hash formats  

### 6. Security Report Generator
- Logs all test results  
- Risk classification  
- Security score calculation  
- Recommendations for improvement  

---

## 🔄 WORKFLOW
1. User selects a module from CLI  
2. Wordlist is generated or loaded  
3. Hash is extracted (simulated)  
4. Dictionary / brute-force attack is executed  
5. Password strength is analyzed  
6. Results are stored  
7. Final security audit report is generated

   

---

## 📊 FLOWCHART (TEXT)
