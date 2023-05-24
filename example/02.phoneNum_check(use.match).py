import re

def format_phone_number(phone_number):
    pattern = r'^(\d{3})(\d{3,4})(\d{4})$'
    match = re.match(pattern, phone_number)
    if match:
        formatted_number = f"({match.group(1)})-{match.group(2)}-{match.group(3)}"
        return formatted_number
    else:
        return "부적합"

phone1 = "1234567890"
phone2 = "010-1234-5678"
phone3 = "12345678"

print(format_phone_number(phone1))  
print(format_phone_number(phone2))
print(format_phone_number(phone3))  
