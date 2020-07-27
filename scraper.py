import requests
from bs4 import BeautifulSoup
import smtplib

result = requests.get("https://globalnews.ca/world/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

links = []
headlines = [] 

for a_tag in soup.find_all("a", class_="c-posts__details"):
    links.append(a_tag['href'])
    span_tag = a_tag.find('span')
    headlines.append(span_tag.text)

l_len = len(links)
h_len = len(headlines)

content = " "
for i in range(h_len):
    content = content + "\n" +  headlines[i] + "\n" + links[i] + "\n"

f = open("news.txt", "w")
f.write(content)
f.close()

