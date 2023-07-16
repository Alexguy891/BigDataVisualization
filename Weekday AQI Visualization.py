import numpy as np
import matplotlib.pyplot as plt


"""debug note: if the length of hours, aqi2023, and aqi2022 do not all match, the code will throw a an error that reads
   'ValueError: could not broadcast input array from shape (#,) into shape (#,)' 
   This can be corrected by making sure the arrays are the same length.
"""

# create a range of hours across a weekday
hours = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#dummy data that shows higher levels in 2023 than 2022
aqi2023 = [232, 216, 159, 125, 98.6, 86.7, 82.3, 71.4, 65.2, 50, 51, 44, 100]
aqi2022 = np.random.randint(10, 50, size = len(hours)) 

fig, ax = plt.subplots(figsize = (9, 9))


#plot 2022 and 2023 and add a line between two points
ax.hlines(y=hours, xmin = aqi2022, xmax = aqi2023, color = 'b', zorder = 1)
ax.plot(aqi2023, hours, 'bo', label='Today\'s AQI', markersize = 10, linewidth = 10)
ax.plot(aqi2022, hours, 'go', label='One Year Ago', markersize = 10, linewidth = 10)
ax.legend(loc = 'upper right', borderpad = 1, fontsize = 15, framealpha = 1)

#Label Graph
#This will return an error if xticks is not the same length of xticklabels or yticks is not the same length as yticktables
ax.set_xlim(left = 0, right = 500)
ax.set_xticks([25.5, 75.5, 125, 175, 250, 400])
ax.set_xticklabels(["Good", "Moderate", "Unhealthy \n for Sensitive \n Groups", "Unhealthy", "Very Unhealthy", "Hazardous"], fontsize = 12)

ax.set_yticks(hours)
ax.set_yticklabels(["8:00pm", "7:00pm", "6:00pm", "5:00pm", "4:00pm", "3:00pm", "2:00pm", "1:00pm", "12:00pm", "11:00am", "10:00am", "9:00am", "8:00am"], fontsize = 12)

ax.set_title('Today At A Glance', fontsize = 20)

# hex codes are taken directly from NOAA manual 
ax.axvspan(0, 51, facecolor = "#00e400", alpha = 0.5)
ax.axvspan(51, 100, facecolor = "#ffff00", alpha = 0.5)
ax.axvspan(100, 150, facecolor = "#ff7e00", alpha = 0.5) 
ax.axvspan(150, 200, facecolor = "#ff0000", alpha = 0.5)
ax.axvspan(200, 300, facecolor = "#8f3f97", alpha = 0.5)
ax.axvspan(300, 500, facecolor = "#7e0023", alpha = 0.5)

plt.tight_layout(pad = 2.0)
plt.show()