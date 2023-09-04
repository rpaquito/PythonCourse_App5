import requests
from send_email import send_email

topic = "tesla"

api_key = "09153fbe28d446f1a087a2b63f4ed1c4"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&sortBy=publishedAt" \
      "&language=en" \
      "&apiKey=09153fbe28d446f1a087a2b63f4ed1c4"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + body + article["title"] + "\n" \
               + str(article["description"]) + "\n" \
               + str(article["url"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
