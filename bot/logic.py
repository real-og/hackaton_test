from datetime import datetime
import calendar

def get_current_month_and_year():
    current_date = datetime.now()

    current_year = current_date.year
    current_month = current_date.strftime("%B")  

    return current_year, current_month


def create_month_table(year, month):
    first_day_of_month = calendar.weekday(year, month, 1)  
    _, last_day_of_month = calendar.monthrange(year, month)

    month_table = []

    weekdays_abbr = calendar.day_abbr
    month_table.append(list(weekdays_abbr))

    current_day = 1
    week_row = []
    for day in range(first_day_of_month):
        week_row.append(0)
    
    while current_day <= last_day_of_month:
        week_row.append(current_day)
        current_day += 1
        if len(week_row) == 7:
            month_table.append(week_row.copy())
            week_row.clear()

    if week_row:
        while len(week_row) < 7:
            week_row.append(0)
        month_table.append(week_row)

    return month_table

def get_next_month_year_pair(month, year, inc):
    if month + inc == 13:
        return 1, year + 1
    elif month + inc == 0:
        return 12, year - 1
    else:
        return month + inc, year
        
