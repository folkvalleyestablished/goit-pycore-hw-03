from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(
            user["birthday"],
            "%Y.%m.%d"
        ).date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1
            )

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:

            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result


users = [
    {"name": "John Doe", "birthday": "2000.07.23"},
    {"name": "Jane Smith", "birthday": "1999.04.19"},
]

print(get_upcoming_birthdays(users))
