# from textblob import TextBlob

# quote1 = """It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."""

# quote2 = """Darcy, as well as Elizabeth, really loved them; and they were both ever sensible of the warmest gratitude towards the persons who, by bringing her into Derbyshire, had been the means of uniting them."""

# sentiment1 = TextBlob(quote1).sentiment
# sentiment2 = TextBlob(quote2).sentiment

# print(quote1 + " has a sentiment of " + str(sentiment1))
# print(quote2 + " has a sentiment of " + str(sentiment2))

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# URL of the webpage
url = "https://www.gutenberg.org/files/1342/1342-h/1342-h.htm"

# Fetch webpage
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Remove metadata, scripts, and styles
for tag in soup(["script", "style", "meta", "noscript", "header", "footer", "link"]):
    tag.decompose()

# Extract only the visible text
text = soup.get_text(separator="\n", strip=True)

# Save to txt file
with open("gutenberg.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Webpage saved as webpage_clean.txt (metadata removed)")

with open("gutenberg.txt", "r", encoding="utf-8") as fileR:
    textR = fileR.read()

blob = TextBlob(textR)

positive_messages = []
negative_messages = []

for i, sentence in enumerate(blob.sentences, start=1):
    polarity = sentence.sentiment.polarity
    if polarity == 1:
        positive_messages.append(sentence)
    if polarity == -1:
        negative_messages.append(sentence)

print("The " + str(len(positive_messages)) + " most positive sentences:")
for sentence in positive_messages:
    print("+ " + str(sentence.replace("\n", "").replace("      ", " ")))
print("The " + str(len(negative_messages)) + " most negative sentences:")
for sentence in negative_messages:
    print("- " + str(sentence.replace("\n", "").replace("      ", " ")))
    
print(len(positive_messages))
print(len(negative_messages))
print(positive_messages)
print(negative_messages)
    



