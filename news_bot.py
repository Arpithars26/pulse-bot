import requests

API_KEY = "9c1d2e90df6540609399721e49c2289b"

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
    date = article["publishedAt"]

    html += f"""
    <h3>{title}</h3>
    <p>Published: {date}</p>
    <a href="{link}">Read Full Article</a>
    <hr>
    """

html += """
</body>
</html>
"""

with open("news_email.html", "w", encoding="utf-8") as file:
    file.write(html)

print("HTML file created successfully")