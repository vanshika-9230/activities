'''Write a Python class,

MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.

Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type

If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class'''
class MedPlus:
    def __init__(self, name: str, batch_number: int, price: float):
        if not isinstance(name, str):
            raise TypeError("name of medicine should be in string")
        if not isinstance(batch_number, int):
            raise TypeError("batch_number of the medicine should be in integers")
        if not isinstance(price, float):
            raise TypeError("price  of medicine should be in float")
        self.name = name
        self.batch_number = batch_number
        self.price = price
 
a=MedPlus("senarest",30,34.5)
print(a.name)



