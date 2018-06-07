import json
import sys
import datetime

# save current json
parsed = ""

# TODO: handle brunch on weekends
# meal periods to search for
periods = ["Breakfast", "Lunch", "Dinner"]

# inspired by: http://love-python.blogspot.com/2010/09/python-code-to-generate-dates-in-range.html
# return a list of dates to parse for
def generate_dates(start_date, end_date):
    td = datetime.timedelta(hours=24)
    current_date = start_date
    date_list = []
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += td

    return date_list

# save list of dates being analyzed
date_list = []

# search for food item in the JSON
def search(cheesecake, date):

    # for each meal period
    for period in periods:
        hall_list = parsed[period]  # get the dining halls
        for hall in hall_list:
            food_list = hall_list[hall]     # get the food-items served
            for item in food_list:
                if cheesecake in item.lower():  # try to match the search query
                    r = "Yay! There's " + item + " at " + hall + " for " + period + " on " + date
                    return r

    return None
    
def main():

    global parsed
    global date_list

    if(len(sys.argv) != 2):
        print("pass a food item to the script")
        sys.exit()

    # food item to search for
    item = sys.argv[1]

    # Set the dates you want to analyze here
    start_date = datetime.date(2018, 6, 6)
    end_date = datetime.date(2018, 6, 14)
    date_list = generate_dates(start_date, end_date)

    # go through each date
    for date in date_list:

        # open the file, and call the function
        filename = "dates/" + date + ".json"
        file = open(filename, "r")
        parsed = json.load(file)
        result = search(item, date)
        if(result):
            print(search(item, date))

if __name__ == "__main__":
    main()
