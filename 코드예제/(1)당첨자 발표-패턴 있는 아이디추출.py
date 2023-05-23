import requests
from bs4 import BeautifulSoup
import re

url = requests.get(
    'http://m.yes24.com/Event/EventWinnerDetail?iContentNo=59080&NoticeYn=Y')
soup = str(BeautifulSoup(url.text, "html.parser"))

result = re.findall(r"[a-zA-Z0-9]+\*{3}", soup)
for i in result:
    print(i)
