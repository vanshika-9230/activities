'''Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) '''

meter=int(input("enter value in meter: "))
a=input("convert meter in: ")
if a=="centimeter":
    print(meter*0.01)
if a=="millimeter":
    print(meter*0.001)
if a=="nanometer":
    print(meter*(10**9))
if a=="kilometer":
    print(meter*1000)
if a=="hectometer":
     print(meter*100)