import requests
from bs4 import BeautifulSoup
import json
import datetime

# base url to request
url = "http://menu.dining.ucla.edu/Menus/"

# TODO: weekend brunch and dinner
# dining periods
periods = ["Breakfast", "Lunch", "Dinner"]

# return a list of dates to parse for
def generate_dates(start_date, end_date):
    td = datetime.timedelta(hours=24)
    current_date = start_date
    date_list = []
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += td

    return date_list

# create a dictionary to hold all menu items for a day
day_cache = dict()

# generate dates and save them to iterate through the menus
date_list = []
# SET start and end dates
start_date = datetime.date(2018, 6, 6)
end_date = datetime.date(2018, 6, 14)
date_list = generate_dates(start_date, end_date)

# iterate through each date
for date in date_list:

    # iterate through each meal period
    for meal_period in periods:

        # create request URL for the day
        req_url = req_url = url + date + "/" + meal_period

        # get the html
        page = requests.get(req_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        cache = dict()  # save food lists to dining halls for each meal period

        # iterate through each dining hall
        for hall in soup.find_all('div',{'class':'menu-block'}):

            hallName = hall.find('h3', {'class':'col-header'}).string  # get name of dining hall
            food_list = []
            # iterate through food items at each hall
            for food in hall.find_all('a',{'class':'recipelink'}):
                food_list.append(food.string)

            cache[hallName] = food_list

        day_cache[meal_period] = cache

    # save the jsons
    filename = "dates/" + date + ".json"
    with open(filename, 'w') as outfile:
    	json.dump(day_cache, outfile)
