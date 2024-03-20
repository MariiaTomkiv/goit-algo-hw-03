from datetime import datetime

users = [
        {"name": "Mariia Tomkiv", "birthday": "1981.03.26"},
        {"name": "Jon Silver", "birthday": "1981.03.25"},
        {"name": "Oksana Gural", "birthday": "1976.01.03"}
        ]
def prepeared_users_birthday(users):
        prepared_users = []
        today = datetime.today().date()
        for user in users:
                birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
                birthday = birthday.replace(year=today.year)
                if birthday < today:
                        birthday = birthday.replace(year=today.year+1)
                diference = (birthday - today).days
                if diference < 7:
                        week_day = birthday.strftime("%A")
                        if week_day == "Saturday" or week_day == "Sunday":
                                                    week_day == "Monday"
                        prepared_users.append({"name": user["name"], "congratulation_date": user["birthday"]})
        print(prepared_users)

prepeared_users_birthday(users)