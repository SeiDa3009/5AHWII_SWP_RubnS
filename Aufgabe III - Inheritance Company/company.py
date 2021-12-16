import company_data as cd
import random

persons = []
staff = []
head_of_departments = []


def add_person():
    return cd.Person(random.choice(list(cd.Gender)), "NDF", "NDF", random.choice(list(cd.Department)))


def add_staff():
    return cd.Staff(random.choice(list(cd.Gender)), "NDF", "NDF", random.choice(list(cd.Department)),
                    random.randint(1, 1000))


def add_head_of_department():
    return cd.HeadOfDepartment(random.choice(list(cd.Gender)), "NDF", "NDF", random.choice(list(cd.Department)),
                               random.randint(1, 1000), "rights")


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
    return (round(male / (len(persons) + len(staff) + len(head_of_departments)), 2)), (round(
        (len(persons) + len(staff) + len(head_of_departments) - male) / (len(persons) + len(staff) + len(head_of_departments)), 2))


if __name__ == '__main__':
    persons = [add_person() for x in range(random.randint(1, 10))]
    staff = [add_staff() for x in range(random.randint(1, 10))]
    head_of_departments = [add_head_of_department() for x in range(random.randint(3, 6))]
    print("Staff: " + str(get_amount()[0]))
    print("Head of department: " + str(get_amount()[1]))
    print("Amount of departments: " + str(get_department()))
    print("Amount of Employees in each Department: ")
    for d in cd.Department:
        print(str.upper(d._name_) + " " + str(get_department_with_most_people(d)))
    txt = "Male-Percentage {:.0%}"
    print(txt.format(male_female_percentage()[0]))
    txt = "Female-Percentage {:.0%}"
    print(txt.format(male_female_percentage()[1]))

