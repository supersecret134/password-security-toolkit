from datetime import datetime

def generate_report(results):
    with open("results/report.txt", "w") as f:

        # ================= HEADER =================
        f.write("=============================================\n")
        f.write("🔐 PASSWORD SECURITY AUDIT REPORT\n")
        f.write("=============================================\n\n")

        f.write("Project: Password Cracking & Credential Attack Suite\n")
        f.write(f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        # ================= OBJECTIVE =================
        f.write("📌 Objective\n")
        f.write("=============================================\n")
        f.write("This audit evaluates password strength and vulnerabilities\n")
        f.write("using simulated dictionary and brute-force attacks.\n\n")

        # ================= METHODOLOGY =================
        f.write("🛠 Methodology\n")
        f.write("=============================================\n")
        f.write("- Password Strength Analysis\n")
        f.write("- Dictionary Attack Simulation\n")
        f.write("- Brute Force Attack Simulation\n")
        f.write("- Hash Extraction (Demo)\n\n")

        # ================= FINDINGS =================
        f.write("🔍 Findings\n")
        f.write("=============================================\n")

        compromised = 0
        total_tests = 0

        # severity counters
        high = 0
        medium = 0
        low = 0

        for r in results:
            total_tests += 1

            if "Password Check" in r:
                if "Weak" in r:
                    f.write(f"[HIGH RISK] {r}\n")
                    compromised += 1
                    high += 1

                elif "Medium" in r:
                    f.write(f"[MEDIUM RISK] {r}\n")
                    medium += 1

                else:
                    f.write(f"[LOW RISK] {r}\n")
                    low += 1

            elif "SUCCESS" in r:
                f.write(f"[HIGH RISK] {r}\n")
                compromised += 1
                high += 1

            elif "Hash Extraction" in r:
                f.write(f"[INFO] {r}\n")
                total_tests -= 1

            else:
                f.write(f"[LOW RISK] {r}\n")
                low += 1

        # ================= SUMMARY =================
        f.write("\n=============================================\n")
        f.write("📊 Summary\n")
        f.write("=============================================\n")

        f.write(f"Total Tests Conducted   : {total_tests}\n")
        f.write(f"Compromised Credentials : {compromised}\n")

        # improved scoring logic
        if compromised > 0:
            security_score = max(0, 70 - (compromised * 20))
        else:
            security_score = 90

        f.write(f"Security Score          : {security_score}%\n\n")

        # severity breakdown
        f.write("Issue Breakdown:\n")
        f.write(f"High Risk Issues   : {high}\n")
        f.write(f"Medium Risk Issues : {medium}\n")
        f.write(f"Low Risk Issues    : {low}\n\n")

        f.write("Score Interpretation:\n")
        f.write("0–40%   : High Risk\n")
        f.write("40–70%  : Moderate Risk\n")
        f.write("70–100% : Secure\n")

        # ================= RISK ANALYSIS =================
        f.write("\n=============================================\n")
        f.write("⚠️ Risk Analysis\n")
        f.write("=============================================\n")

        if compromised > 0:
            f.write("Weak or compromised credentials detected.\n")
            f.write("System is vulnerable to dictionary-based attacks.\n")
            f.write("Presence of even a single compromised credential significantly increases attack risk.\n")
        else:
            f.write("No critical vulnerabilities detected.\n")

        f.write("\nAttackers may exploit weak credentials using automated tools.\n")

        # ================= RECOMMENDATIONS =================
        f.write("\n=============================================\n")
        f.write("✅ Security Recommendations\n")
        f.write("=============================================\n")

        f.write("- Use passwords with 12–16+ characters\n")
        f.write("- Include uppercase, lowercase, numbers, and symbols\n")
        f.write("- Avoid predictable patterns (names, dates)\n")
        f.write("- Enable Multi-Factor Authentication (MFA)\n")
        f.write("- Implement account lockout policies\n")

        # ================= DISCLAIMER =================
        f.write("\n=============================================\n")
        f.write("📘 Disclaimer\n")
        f.write("=============================================\n")
        f.write("This tool is for educational and ethical use only.\n")

        # ================= FOOTER =================
        f.write("\n=============================================\n")
        f.write("End of Report\n")
        f.write("=============================================\n")

    print("✅ Professional report generated successfully!")
