import datetime



def generate_dates(start_date, end_date):
    td = datetime.timedelta(hours=24)
    current_date = start_date
    date_list = []
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += td

    return date_list

start_date = datetime.date(2018, 6, 6)
end_date = datetime.date(2018, 6, 14)
generate_dates(start_date, end_date)
