

"""
Hello World Class
"""

class classHelloWorld:
    def __init__(self, name, dept, roll, gpa):
        self.name = name
        self.dept = dept
        self.roll = roll
        self.gpa = gpa

    def print(self):
        name1 = self.name
        print("The name is " + str(name1))
        print("The dept is " + str(self.dept))
        print("The roll is " + str(self.roll))
        print("The gpa is " + str(self.gpa))

    def loop(self):
        for i in range(self.gpa):
            val = self.gpa
            print("The gpa is " + str(val))


def oprint(name, dept, roll, gpa):
    print("The name is " + str(name))
    print("The dept is " + str(dept))
    print("The roll is " + str(roll))
    print("The gpa is " + str(gpa))