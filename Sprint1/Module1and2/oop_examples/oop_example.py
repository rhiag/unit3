"""A collection of OOP example"""


class BareMinimumClass:
    pass

class Car:
    """An example of a class with attributes and methods"""

    def __inti__(self,fuel,maxspeed,speed=0):
        """This is a constructor(special type of method) that initializes the class. 
        This will be the first method to be run
        It constructs an object from the template/class
        self is a python reserved word. it refers to the class itself
        Speed =0 basically sets speed to 0 by default"""

        """
        Constructor for Car class
        We have a 'fuel' and 'maxspeed' attribute
        
        """

        self.fuel = fuel
        self.maxspeed = maxspeed
        self.speed = speed
    

    def setSpeed(self,new_speed):
        """Method that changes current speed to new value"""
        if new_speed > self.maxspeed:
            return " you cannot exceed maxspeed"
        else:
            self.speed = new_speed
        
    def __repr__(self):
        return "The car speed is {} and it has {} fuel".format(self.speed,self.fuel)


class SocialMediaUser:
    def __init__(self,name,location,upvotes=0):
        """SocialMediaUser Attributes"""
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvotes(self,num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100

# Example of Inheritence

class Animal:
    def __init__(self,name,weight,diet_type):
        self.name = name
        self.weight = float(weight)
        self.diet_type = str(diet_type)

    def run(self):
        return "Me go quick"

    def eat(self,food):
        return "Huge fan of {}".format(food)        

class Sloth(Animal):
    def __init__(self, name, weight, diet_type,num_naps):
        super().__init__(name, weight, diet_type)
        self.num_naps = num_naps

    def run(self):
        """This overrides the run method in Animal"""
        return "I go slow"

    def say_something(self):
        """This is a method exclusive to Sloth and not present in Animal"""
        return "This is a sloth typing"    


 #when you import what is inside the main is not run
print("This is outside the main")

if __name__ == "__main__":
   
    #when you run python oop_example.py is when what is inside the main is run
    print("this is inside the main")

    user1 = SocialMediaUser(name="George Washington", location = "Djibouti",upvotes=2)
    user2 = SocialMediaUser(name="Carlos", location="California",upvotes=20000012334)
    user3 = SocialMediaUser(name="Carmen", location="Texas")

    print(f"user1 is named{user1.name} with {user1.upvotes} upvotes!")
    print(f"Is user1 popular?{user1.is_popular()}")
    user1.recieve_upvotes(200)
    print(f"Is user1 popular?{user1.is_popular()}")


