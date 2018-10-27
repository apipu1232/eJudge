"""Apipu"""
def main():
    """Main function"""
    text = input()
    if 68 <= ord(text) <= 90 or 100 <= ord(text) <= 122:
        print(chr(ord(text) - 3))
    elif 65 <= ord(text) <= 67 or 97 <= ord(text) <= 99:
        print(chr(ord(text) + 23))
    else:
        print(text)
main()