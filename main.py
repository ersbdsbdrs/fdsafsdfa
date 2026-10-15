class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):

    def walk(self):
        print(f"{self.name} ходить")

    def sleep(self):
        print(f"{self.name} спать")

    def study(self):
        print(f"{self.name} study")

    def info(self):
        print(f"{self.name}, ему {self.age}")

if __name__ == '__main__':
    student = Student(name="lala", age= "17")
    student.sleep()
    student.study()
    student.walk()

