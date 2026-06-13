from datetime import datetime

CITY = "Thiruvananthapuram"

quote = "Success is the sum of small efforts repeated day in and day out."
author = "Robert Collier"

today = datetime.now().strftime("%d-%m-%Y")

summary = f"""
PULSE DAILY REPORT
Date: {today}

Location: {CITY}

Motivational Quote:
"{quote}"

- {author}
"""

print(summary)

with open("summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("summary.txt created successfully")