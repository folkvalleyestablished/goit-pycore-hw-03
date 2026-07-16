import re


def normalize_phone(phone_number):
    phone = re.sub(r"\D", "", phone_number)

    if phone.startswith("380"):
        return "+" + phone

    return "+38" + phone


numbers = [
    "067\t123 4567",
    "(095) 234-5678",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050-111-22-22",
]

for number in numbers:
    print(normalize_phone(number))
