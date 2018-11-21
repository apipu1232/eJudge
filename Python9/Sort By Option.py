"""Apipu"""
def main():
    """Main function"""
    name = list()
    surname = list()
    gender = list()
    age = list()
    iden = list()
    grade = list()
    for i in range(20):
        text = input().split()
        name.append(text[0])
        surname.append(text[1])
        gender.append(text[2])
        age.append(text[3])
        iden.append(text[4])
        grade.append(text[5])
    condition = input().lower()
    if condition == "name":
        name, surname, gender, age, iden, grade = zip(*sorted(zip(name, surname, gender, age, \
        iden, grade)))
    if condition == "surname":
        surname, name, gender, age, iden, grade = zip(*sorted(zip(surname, name, gender, age, \
        iden, grade)))
    if condition == "id":
        iden, name, surname, gender, age, grade = zip(*sorted(zip(iden, name, surname, gender, \
        age, grade)))
    for i in range(20):
        if gender[i] == "Male":
            print("Mr", end=" ")
        else:
            print("Miss", end=" ")
        print(name[i][0], end=" ")
        print(surname[i], end=" ")
        print("({0})".format(age[i]), end=" ")
        print("ID:", end=" ")
        print(iden[i], end=" ")
        print("GPA", end=" ")
        print("%.2f"%float(grade[i]))
main()
