import requests

html = requests.get("http://www.hsbi.de")

print(html.text)

# source venv/bin/activate