import numpy as np
import matplotlib.pyplot as plt
from Requests import get_parameter_value
import datetime
def plot_data(data1, data2):
    # Assuming data1 and data2 lists of tuples as shown previously
    values1 = [value for value, unit in data1]
    values2 = [value for value, unit in data2]

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(values1) + 1), values1, label='2022')  # plot for the first month
    plt.plot(range(1, len(values2) + 1), values2, label='2023')  # plot for the second month
    plt.xlabel('Days')
    plt.ylabel('pm25 levels')
    plt.title('Comparison of pm25 levels over the month of June during 2022 and 2023 in NYC')
    plt.legend()

    plt.show()

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
data1 = get_monthly_pm25_data('2022-06-01')
data2 = get_monthly_pm25_data('2023-06-01')
plot_data(data1, data2)