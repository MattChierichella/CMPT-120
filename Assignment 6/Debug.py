class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the c def __int__(self, flavor, frosting):
    def __int__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting
class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    def CarGuess(self):
        if self.model == "Altima":
            print("Your car is a Nissan Altima")
        else:
            print("Hmm that's a car I haven't heard of that car before.")
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Fiona", 11)
    print(newDog.name, newDog.age)
    
    #and what about a new employee
    newEmployee = Employee("Julia", 20133579, "Chemistry")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    
    #now create and print out a cake you make
    newCake = Cake()
    
    #and now create another cake and print it out
    
    
    
    #create a cat!
    cat1 = Cat()
    #create another cat!
    
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.?)
    
    #create a car!
    
    #Now print out the function you made for car :)

main()
