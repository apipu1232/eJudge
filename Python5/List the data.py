"""Apipu"""
def main():
    """Main Function"""
    name = []
    surname = []
    nickname = []
    age = []
    sep = " "
    for _ in range(10):
        text = input()
        text = text.split()
        name.append(text[0])
        surname.append(text[1])
        nickname.append(text[2])
        age.append(text[3])
    print("list of name:", sep.join(name))
    print("list of surname:", sep.join(surname))
    print("list of nickname:", sep.join(nickname))
    print("list of age:", sep.join(age))
main()