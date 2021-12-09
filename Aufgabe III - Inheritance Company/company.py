import company_data as cd
import random

persons = []
staff = []
head_of_departments = []


def add_person():
    return (cd.Person(cd.Gender.male, "Patrick", "Leger", cd.Department.purchase),
                   cd.Person(cd.Gender.male, "Mathew", "Steward", cd.Department.purchase),
                   cd.Person(cd.Gender.male, "Peter", "Pane", cd.Department.production),
                   cd.Person(cd.Gender.female, "Jessica", "Fitzgerald", cd.Department.sell),
                   cd.Person(cd.Gender.female, "Natalie", "Wieg", cd.Department.sell))


def add_staff():
    return (cd.Staff(cd.Gender.female, "Katarina", "Knecht", cd.Department.purchase, random.randint(1,1000)),
                 cd.Staff(cd.Gender.male, "Daniel", "Stöger", cd.Department.production, random.randint(1,1000)),
                 cd.Staff(cd.Gender.male, "Sebastian", "Fieger", cd.Department.production, random.randint(1,1000)),
                 cd.Staff(cd.Gender.male, "Miroslav", "Klose", cd.Department.production, random.randint(1,1000)),
                 cd.Staff(cd.Gender.male, "Mario", "Gomez", cd.Department.purchase, random.randint(1,1000)))


def add_head_of_department():
    return (cd.HeadOfDepartment(cd.Gender.male, "Markus", "Schretter", cd.Department.purchase, random.randint(1,1000),"purchase/production"),
        cd.HeadOfDepartment(cd.Gender.male, "Dietmar", "Kopp", cd.Department.production, random.randint(1,1000),"purchase/production/sell"),
        cd.HeadOfDepartment(cd.Gender.female, "Stephanie", "Himmler", cd.Department.sell, random.randint(1,1000),"production/sell"))

def get_amount():
    return len(staff), len(head_of_departments)

def get_department():
    return len(cd.Department)


def get_department_with_most_people(dep):
    amount = 0
    for p in persons:
        if p.Department == dep:
            amount += 1
    for s in staff:
        if s.Department == dep:
            amount += 1
    for h in head_of_departments:
        if h.Department == dep:
            amount += 1
    return amount


def male_female_percentage():
    male = 0
    for p in persons:
        if p.Gender == cd.Gender.male:
            male += 1
    for s in staff:
        if s.Gender == cd.Gender.male:
            male += 1
    for h in head_of_departments:
        if h.Gender == cd.Gender.male:
            male += 1
    return "%-Male/Female: " + str(
        round(male / (len(persons) + len(staff) + len(head_of_departments)), 2) * 100) + " / " + str(round(
        (len(persons) + len(staff) + len(head_of_departments) - male) / (
                len(persons) + len(staff) + len(head_of_departments)), 2) * 100)


if __name__ == '__main__':
    persons = add_person()
    staff = add_staff()
    head_of_departments = add_head_of_department()
    print("Staff: " + str(get_amount()[0]))
    print("Head of department: " + str(get_amount()[1]))
    print("Amount of departments: " + str(get_department()))
    print("Amount of Employees in each Department: ")
    for d in cd.Department:
        print(str(d._name_) + " " + str(get_department_with_most_people(d)))
    print(male_female_percentage())

