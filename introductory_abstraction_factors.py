'''Factor:  Calculate temperature that a person feels because of the wind (Python3)'''


def factor(temperature, wind_speed):
    
    return  ( 13.12 + 0.6215 * temperature - 11.37 * (wind_speed * 0.16) + 0.3965 * temperature * (wind_speed * 0.16))
temperature=float(input("enter the temperature:"))    
wind_speed=float(input("enter the wind:")) 
print(factor(temperature,wind_speed))