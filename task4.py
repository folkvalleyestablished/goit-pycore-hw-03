from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%d.%m.%Y").date()
        birthday = birthday.replace(year=today.year)
        
        print("todays date: " + str(today))
        print("birthdays date: " + str(birthday))

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        if 0 <= (birthday - today).days <= 7:

            if birthday.weekday() == 5:
                birthday += timedelta(days=2)
            elif birthday.weekday() == 6:
                birthday += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%d.%m.%Y")
            })

    return result


users = [
    {"name": "John Doe", "birthday": "16.07.2000"},
    {"name": "Jane Smith", "birthday": "19.04.1999"},
]

print(get_upcoming_birthdays(users))
