class Student:
    def __init__(self,id,name,student_class,section,shift):
        self.id = id
        self.name = name
        self.student_class = student_class
        self.section = section
        self.shift = shift

    def isPresent(self):
        print(f"{self.name} is present today!")

student1 = Student(1,"Ahsun",10,1,'Morning')

student1.isPresent()