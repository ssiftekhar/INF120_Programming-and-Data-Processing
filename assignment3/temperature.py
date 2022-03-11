import pandas as pd
from matplotlib import pyplot as plt
import math

met12 = pd.read_csv('meteodata_aas_2012.csv', skiprows=1, sep=';')

# plot of temperature
t_avg_array = met12['T_avg'].to_numpy()

x = met12.index
y = t_avg_array 
plt.title("Temperature readings for 2012") 
plt.xlabel("day of year") 
plt.ylabel("Temp [deg C]") 
plt.plot(x,y) 
plt.show()

# Theoretical temperature curve
def year_temp(days):
    t_day = 10 + 20 * math.sin((2*math.pi/365)*(days + 0))
    return t_day

temp_list = []
for i in range(0, 366):
    temp_list.append(year_temp(i))

x = met12.index
y = t_avg_array
y1 = temp_list

plt.title("Temperature readings for 2012") 
plt.xlabel("day of year") 
plt.ylabel("Temp [deg C]") 

plt.plot(x,y, label='Daily average measurement')
plt.plot(x, y1, label='T0 + A * sin(omega*(day + offset))')
plt.legend(loc='upper right')

# Estimation of curve parameters

def year_temp_fit(Tavg, A, offset, days):
    t_day_fit = Tavg + A * math.sin((2*math.pi/365)*(days + offset))
    return t_day_fit

temp_list_fit = []
for i in range(0, 366):
    temp_list_fit.append(year_temp_fit(5, 11, -100, i))

x = met12.index
y2 = t_avg_array
y3 = temp_list_fit

plt.title("Temperature readings for 2012") 
plt.xlabel("day of year") 
plt.ylabel("Temp [deg C]") 

plt.plot(x,y2, label='Daily average measurement')
plt.plot(x, y3, label='T0 + A * sin(omega*(day + offset))')
plt.legend(loc='upper right')
