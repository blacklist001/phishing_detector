phishing_keywords = [
    "urgent", "verify", "suspended", "click", "immediately", "account"
]

def analyze_email(file_path):
    score = 0

    with open(file_path, "r") as file:
        content = file.read().lower()

        for word in phishing_keywords:
            if word in content:
                score += 1

    print(f"Phishing score: {score}")

    if score >= 3:
        print("⚠ Likely PHISHING email")
    else:
        print("✓ Likely legitimate email")

analyze_email("samples/phishing_email.txt")
