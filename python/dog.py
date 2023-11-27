#Anthony D'Antonio
#File for dog class
#Exam 1
#9/11/23

class dog:
    def __init__(self, name, tricks, breed, hungry = True):
      self.name = name
      self.tricks = tricks
      self.breed = breed
      self.hungry = hungry 
   

    def __str__(self) -> str:
       return self.name + ":" + self.breed
      
    def speak(self):
        print("Woof")

    
    def feed(self):
        self.hungry = False

    def add_trick(self,trick):
        self.tricks.append(trick)


    def get_name(self):
        return self.name


    def get_breed(self):
        return self.breed

    def get_tricks(self):
        return self.tricks


    def isHungry(self):
        return self.hungry
