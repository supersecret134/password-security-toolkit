from datetime import datetime

def generate_report(results):
    with open("results/report.txt", "w") as f:
        
        # Header
        f.write("=============================================\n")
        f.write("🔐 PASSWORD SECURITY AUDIT REPORT\n")
        f.write("=============================================\n\n")

        f.write(f"Generated On: {datetime.now()}\n\n")

        f.write("🔍 Findings:\n")

        weak = 0
        total = len(results)

        # ✅ FIXED LOOP
        for r in results:
            if "Password Check" in r:
                if "Weak" in r:
                    f.write(f"[HIGH RISK] {r}\n")
                    weak += 1
                elif "Medium" in r:
                    f.write(f"[MEDIUM RISK] {r}\n")
                else:
                    f.write(f"[LOW RISK] {r}\n")

            elif "SUCCESS" in r:
                f.write(f"[HIGH RISK] {r}\n")
                weak += 1

            else:
                f.write(f"[LOW RISK] {r}\n")

        # Summary
        f.write("\n=============================================\n")
        f.write("📊 Summary\n")
        f.write("=============================================\n")

        f.write(f"Total Passwords Tested : {total}\n")
        f.write(f"Weak Passwords Found  : {weak}\n")

        if total > 0:
            rate = (weak / total) * 100
            f.write(f"Weak Password Rate    : {round(rate,2)}%\n")

        # Risk Analysis
        f.write("\n=============================================\n")
        f.write("⚠️ Risk Analysis\n")
        f.write("=============================================\n")

        f.write("Weak passwords are highly vulnerable to dictionary and brute-force attacks.\n")
        f.write("Attackers can compromise accounts within seconds if weak credentials are used.\n")

        # Recommendations
        f.write("\n=============================================\n")
        f.write("✅ Security Recommendations\n")
        f.write("=============================================\n")

        f.write("- Use passwords with at least 12+ characters\n")
        f.write("- Combine uppercase, lowercase, numbers, and symbols\n")
        f.write("- Avoid common passwords (e.g., admin123, password)\n")
        f.write("- Enable Multi-Factor Authentication (MFA)\n")
        f.write("- Regularly update passwords\n")

        # Footer
        f.write("\n=============================================\n")
        f.write("End of Report\n")
        f.write("=============================================\n")

    print("✅ Professional report generated!")
