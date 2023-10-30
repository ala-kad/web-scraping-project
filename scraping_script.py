import requests
from bs4 import BeautifulSoup, Comment

# URL of the page we want to scrape
url = 'https://www.jeuxvideo.com/forums/42-1000021-72461782-1-0-1-0-les-nouveaux-niveaux-et-ladder-jv.htm'

response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.text

print("Title of the page: ", title)

keyword = 'harcèlement'

occurrences = soup.body(text=lambda text: text and keyword in text.lower())

# Print the number of occurrences found
print("Occurrences of the keyword:", len(occurrences))


# Find all comments within the HTML content
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

# Define the keywords you want to search for
keywords = ['harcèlement']

# Initialize an empty list to store the comments containing the keywords
comments_with_keywords = []

# Loop through each comment and check if it contains any of the keywords
for comment in comments:
    for keyword in keywords:
        if keyword in comment:
            comments_with_keywords.append(comment)
            break  # Exit the inner loop once a keyword is found in the comment

# Print the comments containing the keywords
for comment in comments_with_keywords:
    print("Comment:", comment)
    print("---")

# Print the number of comments containing the keywords
print("Number of comments with keywords:", len(comments_with_keywords))
