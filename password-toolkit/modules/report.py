from datetime import datetime

def generate_report(results):
    with open("results/report.txt", "w") as f:

        # ================= HEADER =================
        f.write("=============================================\n")
        f.write("🔐 PASSWORD SECURITY AUDIT REPORT\n")
        f.write("=============================================\n\n")

        f.write(f"Generated On: {datetime.now()}\n\n")
        f.write("🔍 Findings:\n")

        compromised = 0
        total_tests = 0

        # ================= PROCESS RESULTS =================
        for r in results:

            total_tests += 1

            # Password Strength Check
            if "Password Check" in r:

                if "Weak" in r:
                    f.write(f"[HIGH RISK] {r}\n")
                    compromised += 1

                elif "Medium" in r:
                    f.write(f"[MEDIUM RISK] {r}\n")

                else:
                    f.write(f"[LOW RISK] {r}\n")

            # Attack Success
            elif "SUCCESS" in r:
                f.write(f"[HIGH RISK] {r}\n")
                compromised += 1

            # Hash extraction (info only)
            elif "Hash Extraction" in r:
                f.write(f"[INFO] {r}\n")
                total_tests -= 1  # not a real test case

            else:
                f.write(f"[LOW RISK] {r}\n")

        # ================= SUMMARY =================
        f.write("\n=============================================\n")
        f.write("📊 Summary\n")
        f.write("=============================================\n")

        f.write(f"Total Tests Conducted   : {total_tests}\n")
        f.write(f"Compromised Credentials : {compromised}\n")

        if total_tests > 0:
            risk_rate = (compromised / total_tests) * 100
            security_score = max(0, 100 - risk_rate)

            f.write(f"Security Score          : {round(security_score, 2)}%\n")

        # ================= RISK ANALYSIS =================
        f.write("\n=============================================\n")
        f.write("⚠️ Risk Analysis\n")
        f.write("=============================================\n")

        if compromised > 0:
            f.write("System contains weak or compromised credentials.\n")
            f.write("Immediate password policy enforcement is required.\n")
        else:
            f.write("No critical vulnerabilities detected in current test set.\n")

        f.write("\nAttackers can exploit weak credentials using automated tools.\n")

        # ================= RECOMMENDATIONS =================
        f.write("\n=============================================\n")
        f.write("✅ Security Recommendations\n")
        f.write("=============================================\n")

        f.write("- Use passwords with at least 12+ characters\n")
        f.write("- Combine uppercase, lowercase, numbers, and symbols\n")
        f.write("- Avoid common passwords (admin123, password, etc.)\n")
        f.write("- Enable Multi-Factor Authentication (MFA)\n")
        f.write("- Regularly rotate credentials\n")

        # ================= FOOTER =================
        f.write("\n=============================================\n")
        f.write("End of Report\n")
        f.write("=============================================\n")

    print("✅ Professional report generated successfully!")
