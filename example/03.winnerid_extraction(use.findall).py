# (2) 당첨자 발표 페이지-특정 패턴 가진 아이디 추출(findall 함수 사용)

import requests
from bs4 import BeautifulSoup
import re

url = requests.get(
    'http://m.yes24.com/Event/EventWinnerDetail?iContentNo=59080&NoticeYn=Y')
soup = str(BeautifulSoup(url.text, "html.parser"))

result = re.findall(r"[a-zA-Z0-9]+\*{3}", soup)
for i in result:
    print(i)
