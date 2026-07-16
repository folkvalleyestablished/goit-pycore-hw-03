from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday = birthday.replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        if 0 <= (birthday - today).days <= 7:

            if birthday.weekday() == 5:
                birthday += timedelta(days=2)
            elif birthday.weekday() == 6:
                birthday += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })

    return result


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

print(get_upcoming_birthdays(users))
