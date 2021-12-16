from enum import Enum


class Gender(Enum):
    male = 0,
    female = 1


class Department(Enum):
    purchase = 0,
    production = 1,
    sell = 2


class Person:
    def __init__(self, gender, firstname, lastname, department):
        self.Gender = gender
        self.Firstname = firstname
        self.Lastname = lastname
        self.Department = department


class Staff(Person):
    def __init__(self, gender, firstname, lastname, department, workID):
        super().__init__(gender, firstname, lastname, department)
        self.WorkID = workID


class HeadOfDepartment(Staff):
    def __init__(self, gender, firstname, lastname, department, workID, rights):
        super().__init__(gender, firstname, lastname, department, workID)
        self.Rights = rights


