import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import datetime
from Requests import get_parameter_value

weeks_observed = ["Week 1", "Week 2", "Week 3"]
days_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

days = 21

'''
#Fake Dummy Data
daily_readings = np.array([[1, 12, 26, 52, 120, 200, 400], 
                           [111, 222, 442, 330, 124, 124, 499], 
                           [66, 77, 100, 99, 200, 127, 124]])
'''
hours = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]

#Literally Matt's get_monthly_pm25_data edited for 7 days 
def get_weekly_pm25_data(start_date):
    formatted_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    
    #Visual inspection shows this produces days + 1
    end_date = formatted_date + datetime.timedelta(days=6)

    data = []
    hours = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]


    while formatted_date <= end_date:
        day = formatted_date.strftime('%d')
        month = formatted_date.strftime('%m')
        year = formatted_date.strftime('%Y')

        highest_value = 0

        for i in range(len(hours)): 
            temp_value, unit = get_parameter_value(hours[i], month, day, year, "pm25")
            if temp_value > highest_value: 
                highest_value = temp_value
        data.append(highest_value)

        formatted_date += datetime.timedelta(days=1)

    return data

#00, 01, 02, 03, 08, 

#create three 1-dimention array 
week_1 = get_weekly_pm25_data("2023-06-04")
week_2 = get_weekly_pm25_data("2023-06-11")
week_3 = get_weekly_pm25_data("2023-06-18")

#create one 2-d array out of the three 1D arrays 
daily_readings = np.array([week_1, week_2, week_3])

#Create custom color map based on the NOAA color pallete
noaa_colormap = colors.ListedColormap(["#00e40099", "#ffff0099", "#ff7e0099", "#ff000099", "#8f3f9780", "#7e002380"])
noaa_color_category = colors.BoundaryNorm([0, 12.0, 35.4, 55.4, 150.4, 250.4, 500], 6)


#create image 
fig, ax = plt.subplots(figsize = (10, 10))
im = ax.imshow(daily_readings, cmap = noaa_colormap, norm = noaa_color_category)

#set labels
ax.set_title("Maximum Daily PM2.5 Level", fontsize = 18, pad = 20.0)
ax.set_yticks(np.arange(len(weeks_observed)), labels = weeks_observed)
ax.set_xticks(np.arange(len(days_in_week)), labels = days_in_week)
ax.tick_params(top = True, labeltop = True, bottom = False, labelbottom = False)

#set cbar to show NOAA palette 
cbar = ax.figure.colorbar(im, ax = ax, ticks = [6, 23.75, 45.45, 102.95, 200.45, 375], location = "bottom")
cbar.set_ticklabels(["Good", "Moderate", "Unhealthy \n for Sensitive \n Groups", "Unhealthy", "Very \nUnhealthy", "Hazardous"])

map_start_date = 4
num_of_days = 0

#Create heat map cells 
for week in range(len(weeks_observed)):
    for day in range(len(days_in_week)):
        cell_label = "June " + str(map_start_date + num_of_days) + "\n " + str(daily_readings[week, day])
        label = ax.text(day, week, cell_label, ha = "center", va = "center")
        num_of_days = num_of_days + 1


plt.show()
