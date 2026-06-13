import requests
import os

API_KEY = os.environ["NEWS_API_KEY"]

url = f"https://newsapi.org/v2/everything?q=technology&apiKey={API_KEY}"

data = requests.get(url).json()

html = """
<html>
<body>
<h1>Today's Top Headlines</h1>
<hr>
"""

for article in data["articles"][:5]:

    title = article["title"]
    link = article["url"]

    html += f"""
    <h3>{title}</h3>
    <a href="{link}">Read Full Article</a>
    <hr>
    """

html += """
</body>
</html>
"""

with open("news_email.html", "w", encoding="utf-8") as file:
    file.write(html)

print("HTML file created")