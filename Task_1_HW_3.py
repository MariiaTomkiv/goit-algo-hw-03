from datetime import datetime
   
def get_days_from_today():
    try:
        user_date = datetime.strptime(user_input, '%Y-%m-%d')
        current_data = datetime.today()
        delta_days = current_data - user_date
        return(delta_days.days)
    except:
        print("Введіть дату у правильному форматі!")
user_input = input('Введіть дату у форматі PPPP-MM-ДД:')   
print(get_days_from_today())