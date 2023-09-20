#instructions: Something about these if statements aren't giving the desired effect. Look at them and see how to fix them. (Run them yourself and see what the output is!)
#also, we have some input practice!

def main():
    
    #this is a nice solid working one!
    name = input("your name is? ")
    print("Hello,", name)

    #this isn't printing anything :( so sad. what's wrong with her? Why she not printing out?
    color = input("what's your favorite color? ")
    print("Your favorite color is", color)
    
    #I thought i did this right :( can you fix it for me?
    age = input("How old are you?")
    print("You are", age, "years old")
	
    #Start with this one! We have a compilation error :(
    #Side note: you can put these statements in parentheses or not. it's up to you.
    NUMBER = input("Pick a number 0-10")
    if int(NUMBER) > 3:
        print(NUMBER, "is greater than 3")
    elif int(NUMBER) == 3:
        print("3 is equal to 3")
    else:
        print(NUMBER,"is less than 3")
    #There are multiple correct answers and adjustments to this one 
    isFive = input("Pick a number 0-100")
    if int(isFive) > 5:
        print(isFive, "is greater than 5")
    elif int(isFive) == 5:
        print("5 is equal to 5")
    else:
        print(isFive, "is less than 5")
    #more multiple correct answers. Similar to the first. Adjust as perceived 
    toCheck = input("Pick a NUMBBERR!!!!!!! 0-20!")
    if int(toCheck) > 5:
        print(toCheck, "is greater than 5.")
    elif int(toCheck) < 3:
	    print(toCheck, "is less than 3")
    else:
        print(toCheck, "is 3")

    #Is it really printing the BEST option though? Rearrange these as you see fit
    numberz = input("Pick a number 0-100")
    if int(numberz) < 5:
        print(numberz," is less than 5")
    elif int(numberz) > 5:
        print(numberz, "is greater than 5")
    elif int(numberz) == 5:
        print(numberz, "is 5")
    else:
        print(numberz, "is invalid")
    
    
    
    
main()
