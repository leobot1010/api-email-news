import requests
from send_article import send_email

topic = "tesla"
api_key = "31e351419ccb4195b6bcbebad0cf388b"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=31e351419ccb4195b6bcbebad0cf388b&" \
      "language=en"

# MAKE REQUEST
request = requests.get(url)

# GET DATA IN DICTIONARY FORMAT
content = request.json()

# ADD ALL THE TITLE's & DESCRIPTION's TO ONE STRING
body = "Subject: Today's News" + "\n"  # Subject added at the initialization of the body

for article in content["articles"][0:20]:  # reduce to the first 20 articles

    if (article["description"] is not None
            and article['title'] is not None
            and article["title"] != "[Removed]"):  # filters out removed articles

        a = " ".join(article['title'].split())
        d = " ".join(article['description'].split())

        body = (body + a + "\n" + d + "\n"
                + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(body)
