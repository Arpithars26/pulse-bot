import requests
import json

USERNAME = "Arpithars26"

url = f"https://api.github.com/users/{USERNAME}/repos"

repos = requests.get(url).json()

projects = []

for repo in repos:

    projects.append({
        "name": repo["name"],
        "url": repo["html_url"],
        "description": repo["description"]
    })

with open("projects.json", "w", encoding="utf-8") as file:
    json.dump(projects, file, indent=4)

print("projects.json created")