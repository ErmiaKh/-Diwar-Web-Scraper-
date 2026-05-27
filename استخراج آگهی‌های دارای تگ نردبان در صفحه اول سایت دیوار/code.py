import requests
from bs4 import BeautifulSoup
import re

url = "https://divar.ir/s/tehran"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, "html.parser")

text = soup.get_text("\n", strip=True)

pattern = re.compile(r"(.*?نردبان شده.*?)(?:\n|$)", re.DOTALL)

matches = pattern.findall(text)

if matches:
    print("آگهی‌های دارای تگ نردبان:")
    for i, item in enumerate(matches, 1):
        print(f"{i}. {item.strip()}")
else:
    print("هیچ آگهی دارای تگ نردبان پیدا نشد.")
