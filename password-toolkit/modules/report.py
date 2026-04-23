from datetime import datetime

def generate_report(results):
    with open("results/report.txt", "w") as f:

        f.write("=============================================\n")
        f.write("🔐 PASSWORD SECURITY AUDIT REPORT\n")
        f.write("=============================================\n\n")

        f.write(f"Generated On: {datetime.now()}\n\n")
        f.write("🔍 Findings:\n\n")

        compromised = 0
        total_tests = 0

        for r in results:

            # count only real test cases
            if "Password Check" in r or "SUCCESS" in r or "FAILED" in r:
                total_tests += 1

            # ---------------- PASSWORD CHECK ----------------
            if "Password Check" in r:

                if "Weak" in r:
                    f.write(f"[HIGH RISK] {r}\n")
                    compromised += 1

                elif "Medium" in r:
                    f.write(f"[MEDIUM RISK] {r}\n")

                else:
                    f.write(f"[LOW RISK] {r}\n")

            # ---------------- ATTACK SUCCESS ----------------
            elif "SUCCESS" in r:
                f.write(f"[HIGH RISK] {r} (password compromised)\n")
                compromised += 1

            # ---------------- ATTACK FAILED ----------------
            elif "FAILED" in r:
                f.write(f"[SAFE] {r} (no password match found)\n")

            # ---------------- INFO EVENTS ----------------
            elif "Wordlist generated" in r or "Hash Extraction" in r:
                f.write(f"[INFO] {r}\n")

            else:
                f.write(f"[INFO] {r}\n")

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
            f.write("No critical vulnerabilities detected.\n")

        # ================= RECOMMENDATIONS =================
        f.write("\n=============================================\n")
        f.write("✅ Security Recommendations\n")
        f.write("=============================================\n")

        f.write("- Use 12+ character passwords\n")
        f.write("- Mix uppercase, lowercase, numbers, symbols\n")
        f.write("- Avoid common passwords\n")
        f.write("- Enable Multi-Factor Authentication (MFA)\n")
        f.write("- Rotate passwords regularly\n")

        # ================= FINAL VERDICT =================
        f.write("\n=============================================\n")
        f.write("🧠 Final Verdict\n")
        f.write("=============================================\n")

        if compromised > 0:
            f.write("The system has security weaknesses due to compromised credentials.\n")
            f.write("Immediate action is recommended to strengthen password policies.\n")
        else:
            f.write("The system demonstrates a strong security posture based on current tests.\n")

        f.write("\n=============================================\n")
        f.write("End of Report\n")
        f.write("=============================================\n")

    print("✅ Professional report generated successfully!")
