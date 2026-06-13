import requests
from bs4 import BeautifulSoup

sites = {
    "BBC": "https://www.bbc.com/news",
    "CNN": "https://edition.cnn.com",
    "Reuters": "https://www.reuters.com"
}

html_content = """
<html>
<head>
<title>Morning News Digest</title>
</head>
<body>
<h1>Top Headlines</h1>
"""

for source, url in sites.items():

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all(["h1", "h2", "h3"])

        html_content += f"<h2>{source}</h2><ul>"

        count = 0

        for headline in headlines:

            text = headline.get_text().strip()

            if len(text) > 20:

                html_content += f"<li>{text}</li>"

                count += 1

            if count == 3:
                break

        html_content += "</ul>"

    except Exception as e:

        html_content += f"<p>Error reading {source}</p>"

html_content += """
</body>
</html>
"""

with open("news_digest.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("News Digest Created Successfully!")