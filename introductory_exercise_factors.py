'''Factor:  Calculate temperature that a person feels because of the wind (Python3)'''

temperature = float(input("Enter the temperature of air in degrees Celsius: "))
wind_speed = float(input("Enter the speed of  in kilometers per hour: "))

temp_of_wind_chill = 13.12 + 0.6215 * temperature- 11.37 * (wind_speed * 0.16) + 0.3965 * temperature * (wind_speed* 0.16)

print("Wind chill temperature:", temp_of_wind_chill, "degrees Celsius")