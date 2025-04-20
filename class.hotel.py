# here a class named hotel 
class Hotel:


    # define constructor that determine the properties  and feature of class
    def __init__(self,place,rooms,staff,name="the green heaven"):
        self.place=place
        self.rooms=rooms
        self.staff=staff
        self.name=name


        # a method is constructed 
    def describe(self):
        print(f"the hotel is in {self.place},there are {self.rooms}rooms,the number of staff are{self.staff},and the name of the hotel is {self.name}")    

# formation of object of class 
hotel1=Hotel("india","5000","10000","the green heaven")




# call the method 
hotel1.describe() 