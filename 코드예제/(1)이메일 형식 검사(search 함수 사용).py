import re

email_regex = re.compile("^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+$")
email_input = input("이메일을 입력하세요 : ")

if email_regex.search(email_input):
    print("적합")
else:
    print("부적합")