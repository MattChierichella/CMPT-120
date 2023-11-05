
def printHello(y):
    print("Hello")
    return
def printName(x):
    print(x)

def addition(x, y):
    #add x and y together and return them
    print(y, x)
    return
def smaller(i, j):
    #if i is smaller than j, return i
    if i < j:
        return i
    #if j is smaller than i, return j
    elif j < i:
        return j
    #if they're even, return 0
    elif j == i:
        return 0
def main():
    #call the printHello function here
    y = printHello("Hello")
    #call printName and give it the parameter of your name
    x = printName("Matthew")
    var1 = 10
    var2 = 20
    #What do we put in here to make it work?
    print(addition(var1, var2))
    i = int(input("Enter number 1"))
    j = int(input("Enter number 2"))
    #what go here?
    print(smaller(i, j))
main()
