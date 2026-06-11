from datetime import date
import requests

# Today's date
today = date.today()

# Weather
try:
    weather = requests.get(
        "https://wttr.in/Thiruvananthapuram?format=3&m",
        timeout=10
    ).text
except Exception:
    weather = "Weather unavailable"

# Quote
try:
    quote_data = requests.get(
        "https://zenquotes.io/api/random",
        timeout=10
    ).json()

    quote = quote_data[0]["q"]
    author = quote_data[0]["a"]

except Exception:
    quote = "Keep learning and keep building."
    author = "Task Bot"

quote = quote_data[0]["q"]
author = quote_data[0]["a"]

# Output
summary = f"""PULSE - Daily Summary

Date: {today}

WEATHER
{weather}

QUOTE
{quote}
- {author}
"""

with open("daily_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("Daily summary saved successfully!")