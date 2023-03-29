'''Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) '''

def conversion(fahrnit):
   c=(fahrnit-32)*(5/9)#c is denoting the celcius
   return c
    
fahrnit=float(input("enter value in fahrnit: "))
print(conversion(fahrnit))