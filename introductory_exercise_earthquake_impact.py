'''Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)'''
magnitude_of_waves=float(input("Enter speed: km/h"))

if magnitude_of_waves < 2:
    print("No imapct, but recorded")
if magnitude_of_waves >= 2 and magnitude_of_waves < 4:
    print("Felt, by few people")
if magnitude_of_waves  >= 4 and magnitude_of_waves< 6:
    print("Felt by people, but no damage.")
if magnitude_of_waves  >= 6 and magnitude_of_waves<  7:
    print("Light damage.")
if magnitude_of_waves  >= 7 and magnitude_of_waves< 8:
    print("Moderate damage.")
if magnitude_of_waves >= 8 and magnitude_of_waves<10:
    print("Severe damage.")
if magnitude_of_waves >= 10 and magnitude_of_waves< 13:
    print("Major earthquake.")
if magnitude_of_waves>13:
    print("Great earthquake, can have more and more destruction.")
