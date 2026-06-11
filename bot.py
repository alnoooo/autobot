from datetime import date
import requests

# Today's date
today = date.today()

# Weather
weather = requests.get(
    "https://wttr.in/Thiruvananthapuram?format=3"
).text

# Quote
quote_data = requests.get(
    "https://zenquotes.io/api/random"
).json()

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