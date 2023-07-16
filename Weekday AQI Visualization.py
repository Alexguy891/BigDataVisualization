import numpy as np
import matplotlib.pyplot as plt
from Requests import get_parameter_value

#Requests must have an uppercase R, otherwise it will import requests library


"""debug note: if the length of hours, aqi2023, and aqi2022 do not all match, the code will throw a an error that reads
   'ValueError: could not broadcast input array from shape (#,) into shape (#,)' 
   This can be corrected by making sure the arrays are the same length.
"""


def get_hourly_reading(start_hour, hours_needed, start_month, start_day, start_year):
   hourly_ppm25 = []

   for i in range(hours_needed):
      current_hour = start_hour + i

      #convert int current_hour to string format used in get_parameter_value
      if current_hour < 10:
         current_hour_string = "0" + str(current_hour)
      else:
         current_hour_string = str(current_hour)

      current_ppm25, unit = get_parameter_value(current_hour_string, start_month, start_day, start_year, "pm25")
      hourly_ppm25.append(current_ppm25)
   
   return hourly_ppm25
      
# create a range of hours across a weekday
hours = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number_of_hours = len(hours)

ppm25_2023 = get_hourly_reading(8, number_of_hours, "06", "07", "2023")
ppm25_2022 = get_hourly_reading(8, number_of_hours, "06", "07", "2022")


#dummy data that shows higher levels in 2023 than 2022
#aqi2023 = [232, 216, 159, 125, 98.6, 86.7, 82.3, 71.4, 65.2, 50, 51, 44, 100]
#aqi2022 = np.random.randint(10, 50, size = len(hours)) 


fig, ax = plt.subplots(figsize = (12, 9))


#plot 2022 and 2023 and add a line between two points
ax.hlines(y=hours, xmin = ppm25_2022, xmax = ppm25_2023, color = 'b', zorder = 1)
ax.plot(ppm25_2023, hours, 'bo', label='Today\'s Air Quality', markersize = 10, linewidth = 10)
ax.plot(ppm25_2022, hours, 'go', label='One Year Ago', markersize = 10, linewidth = 10)
ax.legend(loc = 'upper right', borderpad = 1, fontsize = 15, framealpha = 1)

#Label Graph
#This will return an error if xticks is not the same length of xticklabels or yticks is not the same length as yticktables
ax.set_xlim(left = 0, right = 420.0)
ax.set_xticks([6, 23.75, 45.45, 102.95, 200.45, 335.25])
ax.set_xticklabels(["Good", "Moderate", "Unhealthy \n for Sensitive \n Groups", "Unhealthy", "Very \nUnhealthy", "Hazardous"], fontsize = 11, rotation = -60, ha = "center")

ax.set_yticks(hours)
ax.set_yticklabels(["8:00pm", "7:00pm", "6:00pm", "5:00pm", "4:00pm", "3:00pm", "2:00pm", "1:00pm", "12:00pm", "11:00am", "10:00am", "9:00am", "8:00am"], fontsize = 11)

ax.set_title('Today At A Glance', fontsize = 20)

# hex codes are taken directly from NOAA manual 
ax.axvspan(0, 12.0, facecolor = "#00e400", alpha = 0.5)
ax.axvspan(12.0, 35.4, facecolor = "#ffff00", alpha = 0.5)
ax.axvspan(35.4, 55.4, facecolor = "#ff7e00", alpha = 0.5) 
ax.axvspan(55.4, 150.4, facecolor = "#ff0000", alpha = 0.5)
ax.axvspan(150.4, 250.4, facecolor = "#8f3f97", alpha = 0.5)
ax.axvspan(250.4, 420.0, facecolor = "#7e0023", alpha = 0.5)

plt.tight_layout(pad = 2.0)
plt.show()