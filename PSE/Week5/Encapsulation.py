class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__grade = 'A'
        self.__private = 'Private'

    def get_grade(self):
        return self.__grade
    
    def get_private(self):
        return self.__private

class International(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def get_age(self):
        return self._age
    
class lecturer:
    def __init__(self, lecName, lecAge):
        self.lecName = lecName
        self._lecAge = lecAge
        self.__irdNumber = "IRD403454"

    def get_irdNumber(self):
        return self.__irdNumber
    

def main():
    #Creating a Student
    s = Student("Lea", 20)
    print("Student name " + s.name + " Age " + str(s._age))
    print("Grade: " + str(s.get_grade()))
    print("Private: " + str(s.get_private()))


    I = International("Henry", 11)
    print("Name: " + I.name + " Age: " + str(I.get_age()))


    l = lecturer("Rao", 20)
    print("Lecturer name " + l.lecName + " Age " + str(l._lecAge))
    
    print("IRD Number: " + l.get_irdNumber())

if __name__ == "__main__":
    main()
