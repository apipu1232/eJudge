"""Apipu"""
def main():
    """Main Function"""
    text = input()
    print(chr((ord(text) + 23) * (99 >= ord(text) >= 97)\
        + (ord(text) - 3) * (122 >= ord(text) >= 100) + (ord(text) *\
        (96 >= ord(text) or ord(text) >= 123))))
main()