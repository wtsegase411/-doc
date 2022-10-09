import requests
from bs4 import BeautifulSoup

# target url
url = 'http://www.google.com'

# making requests instance
reqs = requests.get(url)

# using the BeautifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')

# displaying the title
print("Title of the website is : ")
for title in soup.find_all('title'):
    print(title.get_text())