import numpy as np
import matplotlib.pyplot as plt
from Requests import get_parameter_value
import datetime
def get_monthly_pm25_data(start_date):
    formatted_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')

    end_date = formatted_date + datetime.timedelta(days=30)

    data = []

    while formatted_date <= end_date:
        day = formatted_date.strftime('%d')
        month = formatted_date.strftime('%m')
        year = formatted_date.strftime('%Y')
        value, unit = get_parameter_value("12", month, day, year, "pm25")
        data.append((value, unit))

        formatted_date += datetime.timedelta(days=1)

    return data
#Requests must have an uppercase R, otherwise it will import requests library
data = get_monthly_pm25_data('2023-06-01')
for value, unit in data:
    print("Value: ", value, "Unit: ", unit)
value, unit = get_parameter_value('12', '06', '07', '2023', 'pm25')
       
print(value, unit)