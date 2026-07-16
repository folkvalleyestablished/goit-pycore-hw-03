from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - date).days
    except:
        return "Неправильна дата"


print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2020/10/09"))
