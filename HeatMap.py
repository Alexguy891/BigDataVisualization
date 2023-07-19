import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from Requests import get_parameter_value

weeks_observed = ["Week 1", "Week 2", "Week 3"]
days_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

days = 21

daily_readings = np.array([[1, 12, 26, 52, 120, 200, 400], 
                           [111, 222, 442, 330, 124, 124, 499], 
                           [66, 77, 100, 99, 200, 127, 124]])

noaa_colormap = colors.ListedColormap(["#00e40099", "#ffff0099", "#ff7e0099", "#ff000099", "#8f3f9780", "#7e002380"])
noaa_color_category = colors.BoundaryNorm([0, 12.0, 35.4, 55.4, 150.4, 250.4, 500], 6)


fig, ax = plt.subplots(figsize = (10, 10))
im = ax.imshow(daily_readings, cmap = noaa_colormap, norm = noaa_color_category)


ax.set_yticks(np.arange(len(weeks_observed)), labels = weeks_observed)
ax.set_xticks(np.arange(len(days_in_week)), labels = days_in_week)
ax.tick_params(top = True, labeltop = True, bottom = False, labelbottom = False)

start_date = 6

cbar = ax.figure.colorbar(im, ax = ax, ticks = [6, 23.75, 45.45, 102.95, 200.45, 375], location = "bottom")
cbar.set_ticklabels(["Good", "Moderate", "Unhealthy \n for Sensitive \n Groups", "Unhealthy", "Very \nUnhealthy", "Hazardous"])

map_start_date = 6
num_of_days = 0

for week in range(len(weeks_observed)):
    for day in range(len(days_in_week)):
        cell_label = "June " + str(map_start_date + num_of_days) + "\n " + str(daily_readings[week, day])
        label = ax.text(day, week, cell_label, ha = "center", va = "center")
        num_of_days = num_of_days + 1


plt.show()
