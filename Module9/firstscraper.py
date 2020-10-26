import requests
from bs4 import BeautifulSoup

url = "https://www.dmacc.edu/schedule/Pages/result.aspx?Term=201903&Campus=1;4&S"
response = requests.get(url)
html = response.content
f = open("requestsResult.txt", "w+")
f.writelines(str(html))
f.close()

with open("requestsResult.txt") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print(soup.prettify())



