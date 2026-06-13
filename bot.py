import requests

def get_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)

    data = response.json()

    quote = data[0]["q"]
    author = data[0]["a"]

    return f'"{quote}" - {author}'

def get_weather():
    url = "https://wttr.in/?format=3"
    response = requests.get(url)

    return response.text

def create_summary():

    weather = get_weather()
    quote = get_quote()

    summary = f"""
DAILY SUMMARY

Weather:
{weather}

Quote:
{quote}
"""

    with open("summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    print("Summary saved!")

create_summary()