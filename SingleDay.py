import numpy as np
import matplotlib.pyplot as plt
import datetime
from Requests import get_parameter_value

#Requests must have an uppercase R, otherwise it will import requests library

def get_hourly_pm25_data(start_time):
    formatted_time = datetime.datetime.strptime(start_time, '%H-%Y-%m-%d')

    end_time = formatted_time + datetime.timedelta(hours=12)

    data = []

    while formatted_time <= end_time:
        hour = formatted_time.strftime('%H')
        day = formatted_time.strftime('%d')
        month = formatted_time.strftime('%m')
        year = formatted_time.strftime('%Y')
        value, unit = get_parameter_value(hour, month, day, year, "pm25")
        data.append((value))

        formatted_time+= datetime.timedelta(hours=1)
    return data

def run_aqi_visualization():
    # test_data = get_hourly_pm25_data("08-2023-06-07")
    # print(test_data)
    # test_data_2022 = get_hourly_pm25_data("08-2022-06-07")


    # create a range of hours across a weekday
    hours = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    number_of_hours = len(hours)


    #Get data
    ppm25_2023 = get_hourly_pm25_data("08-2023-06-07")
    ppm25_2022 = get_hourly_pm25_data("08-2022-06-07") 


    fig, ax = plt.subplots(figsize = (12, 9))


    #plot 2022 and 2023 and add a line between two points
    ax.hlines(y=hours, xmin = ppm25_2022, xmax = ppm25_2023, color = 'b', zorder = 1)
    ax.plot(ppm25_2023, hours, 'bo', label='Today\'s Air Quality', markersize = 10, linewidth = 10)
    ax.plot(ppm25_2022, hours, 'go', label='One Year Ago', markersize = 10, linewidth = 10)
    ax.legend(loc = 'best', borderpad = 1, fontsize = 15, framealpha = 1)

    #Label Graph
    #This will return an error if xticks is not the same length of xticklabels or yticks is not the same length as yticktables
    ax.set_xlim(left = 0, right = 420.0)
    ax.set_xticks([6, 23.75, 45.45, 102.95, 200.45, 335.25])
    ax.set_xticklabels(["Good", "Moderate", "Unhealthy \n for Sensitive \n Groups", "Unhealthy", "Very \nUnhealthy", "Hazardous"], fontsize = 11, rotation = -60, ha = "center")

    ax.set_yticks(hours)
    ax.set_yticklabels(["8:00pm", "7:00pm", "6:00pm", "5:00pm", "4:00pm", "3:00pm", "2:00pm", "1:00pm", "12:00pm", "11:00am", "10:00am", "9:00am", "8:00am"], fontsize = 11)

    ax.set_title('Today\'s Air Quality At A Glance', fontsize = 20)

    # hex codes are taken directly from NOAA manual 
    ax.axvspan(0, 12.0, facecolor = "#00e400", alpha = 0.5)
    ax.axvspan(12.0, 35.4, facecolor = "#ffff00", alpha = 0.5)
    ax.axvspan(35.4, 55.4, facecolor = "#ff7e00", alpha = 0.5) 
    ax.axvspan(55.4, 150.4, facecolor = "#ff0000", alpha = 0.5)
    ax.axvspan(150.4, 250.4, facecolor = "#8f3f97", alpha = 0.5)
    ax.axvspan(250.4, 420.0, facecolor = "#7e0023", alpha = 0.5)

    bbox_props = dict(boxstyle = "square,pad=0.3", facecolor = "#FBF5FF", alpha = 1, edgecolor = "#7e0023", lw = 2)

    ax.text(335.25, 13, "Hazardous: Emergency Conditions. \n Entire population impacted. \n All may experience serious health effects. \nAvoid all outdoor activities.", fontweight = "extra bold", transform = ax.transData, fontsize = 10, verticalalignment = "center", horizontalalignment = "center", bbox = bbox_props, zorder = 3)



    plt.tight_layout(pad = 2.0)
    plt.show()