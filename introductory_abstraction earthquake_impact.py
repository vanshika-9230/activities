'''Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)'''



def earthquake_impact(s_modulus,sm_moment,density ):
    speed_of_seismic_waves=(((s_modulus*s_modulus_moment) / density)**(2))
    return speed_of_seismic_waves 
s_modulus=float(input("shear_modulus: "))
Density=float(input("density: "))  
sm_moment=float(input("seismic_moment: "))
print(earthquake_impact(s_modulus,sm_moment,density ))