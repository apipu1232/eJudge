"""Apipu"""
def main():
    """Main Function"""
    text = input()
    text1 = text.index("r=")
    text2 = text.index("&")
    text3 = text.index("d=")
    user = text[text1+2:text2]
    password = text[text3+2:]
    print(user)
    print(password)
main()
