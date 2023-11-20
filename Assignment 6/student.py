#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''
import random


class student:
    def __init__(self, name, studentid, year, major, gpa):
        self.name = name
        self.studentid = studentid
        self.year = year
        self.major = major
        self.gpa = gpa
    def honorscheck(self):
        if self.gpa >= 3.5:
            return(True)
        else:
            return(False)
    def freefood(self):
        randnum = random.randint(10000, 99999)
        if randnum == self.studentid:
            return((self.name), "won free food!")
        else:
            return("I guess you're starving :(")

    
def main():
    #create three students and check if they get free lunch and if they qualify for honors
    stud1 = student("Matthew", 20146, "Sophomore","Criminal Justice", 3.5)
    stud2 = student("Julia", 20133, "Junior", "Biochemistry", 1.4)
    stud3 = student("Conor", 20147, "Sophomore", "Political Science", 3.9)
    print(stud1.honorscheck())
    print(stud2.honorscheck())
    print(stud3.honorscheck())

    print(stud1.freefood())
    print(stud2.freefood())
    print(stud3.freefood())




    
main()
