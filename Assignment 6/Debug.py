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
    def __init__(self, flavor, frosting):
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
            return("Your car is a Nissan Altima")
        else:
            return("Hmm that's a car I haven't heard of that car before.")
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Fiona", 11)
    print(newDog.name, newDog.age)
    
    #and what about a new employee
    newEmployee = Employee("Julia", 20133597, "Chemistry")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    
    #now create and print out a cake you make
    cake1 = Cake("Chocolate", "Vanilla")
    print(cake1.flavor, cake1.frosting)
    
    #and now create another cake and print it out
    cake2 = Cake("Vanilla", "Blueberry")
    print(cake2.flavor, cake2.frosting)
    
    #create a cat!
    cat1 = Cat("Josie", 10, "no hair")
    #create another cat!
    cat2 = Cat("Chase", 3, "long")
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    print(cat2.breedGuess())
    
    #create a car!
    myCar = Car("Altima", 2014, "White")
    #Now print out the function you made for car :)
    print(myCar.CarGuess())

main()
